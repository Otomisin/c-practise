require([
  "esri/WebMap",
  "esri/Graphic",
  "esri/views/MapView",
  "esri/layers/FeatureLayer",
  "esri/widgets/Legend",
  "esri/widgets/Expand",
  "esri/smartMapping/labels/clusters",
  "esri/smartMapping/popup/clusters",
  "esri/core/reactiveUtils",
  "esri/symbols/support/symbolUtils",
  "esri/geometry/geometryEngine"
], (
  WebMap,
  Graphic,
  MapView,
  FeatureLayer,
  Legend,
  Expand,
  clusterLabelCreator,
  clusterPopupCreator,
  reactiveUtils,
  symbolUtils,
  geometryEngine
) => {
  let layerView;

  const layer = new FeatureLayer({
    portalItem: {
      id: "eb54b44c65b846cca12914b87b315169"
    },
    outFields: ["capacity_mw"]
  });

  const map = new WebMap({
    basemap: {
      portalItem: {
        id: "75a08e8cd8b64dcfa6945bb7f624ccc5"
      }
    },
    layers: [layer]
  });

  const view = new MapView({
    container: "viewDiv",
    map,
    extent: {
      spatialReference: {
        latestWkid: 3857,
        wkid: 102100
      },
      xmin: -15327459,
      ymin: 2740044,
      xmax: -6076744,
      ymax: 6878650
    },
    popup: {
      dockEnabled: true,
      dockOptions: {
        breakpoint: false,
        position: "top-right"
      }
    }
  });

  view.ui.add(
    new Expand({
      content: new Legend({ view }),
      view
    }),
    "top-left"
  );

  layer
    .when()
    .then(generateClusterConfig)
    .then(async (featureReduction) => {
      // sets generated cluster configuration on the layer
      layer.featureReduction = featureReduction;

      // the layer view is needed for querying clusters
      layerView = await view.whenLayerView(layer);
    })
    .catch((error) => {
      console.error(error);
    });

  async function generateClusterConfig(layer) {
    // generates default popupTemplate
    const popupTemplate = await clusterPopupCreator
      .getTemplates({
        layer
      })
      .then(
        (popupTemplateResponse) =>
          popupTemplateResponse.primaryTemplate.value
      );

    // Add actions for exploring the features of each cluster
    popupTemplate.actions = [
      {
        title: "Statistics",
        id: "statistics",
        className: "esri-icon-line-chart"
      },
      {
        title: "Convex hull",
        id: "convex-hull",
        className: "esri-icon-polygon"
      },
      {
        title: "Show features",
        id: "show-features",
        className: "esri-icon-maps"
      }
    ];

    // generates default labelingInfo
    const { labelingInfo, clusterMinSize } = await clusterLabelCreator
      .getLabelSchemes({
        layer,
        view
      })
      .then((labelSchemes) => labelSchemes.primaryScheme);

    return {
      type: "cluster",
      popupTemplate,
      labelingInfo,
      clusterMinSize,
      maxScale: 50000
    };
  }

  reactiveUtils.on(
    () => view.popup,
    "trigger-action",
    (event) => {
      clearViewGraphics();

      const popup = view.popup;
      const selectedFeature =
        popup.selectedFeature && popup.selectedFeature.isAggregate;

      const id = event.action.id;

      if (id === "convex-hull") {
        displayConvexHull(view.popup.selectedFeature);
      }
      if (id === "show-features") {
        displayFeatures(view.popup.selectedFeature);
      }
      if (id === "statistics") {
        calculateStatistics(view.popup.selectedFeature);
      }
    }
  );

  reactiveUtils.watch(
    () => [view.scale, view.popup.selectedFeature, view.popup.visible],
    clearViewGraphics
  );

  let convexHullGraphic = null;
  let clusterChildGraphics = [];

  function clearViewGraphics() {
    view.graphics.remove(convexHullGraphic);
    view.graphics.removeMany(clusterChildGraphics);
  }

  // displays all features from a given cluster in the view
  async function displayFeatures(graphic) {
    processParams(graphic, layerView);

    const query = layerView.createQuery();
    query.aggregateIds = [graphic.getObjectId()];
    const { features } = await layerView.queryFeatures(query);

    features.forEach(async (feature) => {
      const symbol = await symbolUtils.getDisplayedSymbol(feature);
      feature.symbol = symbol;
      view.graphics.add(feature);
    });
    clusterChildGraphics = features;
  }

  async function displayConvexHull(graphic) {
    processParams(graphic, layerView);

    const query = layerView.createQuery();
    query.aggregateIds = [graphic.getObjectId()];
    const { features } = await layerView.queryFeatures(query);
    const geometries = features.map((feature) => feature.geometry);
    const [convexHull] = geometryEngine.convexHull(geometries, true);

    convexHullGraphic = new Graphic({
      geometry: convexHull,
      symbol: {
        type: "simple-fill",
        outline: {
          width: 1.5,
          color: [75, 75, 75, 1]
        },
        style: "none",
        color: [0, 0, 0, 0.1]
      }
    });
    view.graphics.add(convexHullGraphic);
  }

  // calculates set statistics for features in a cluster
  // and displays them in the cluster popup

  async function calculateStatistics(graphic) {
    processParams(graphic, layerView);

    const query = layerView.createQuery();

    query.aggregateIds = [graphic.getObjectId()];

    query.groupByFieldsForStatistics = ["fuel1"];
    query.outFields = ["capacity_mw", "fuel1"];
    query.orderByFields = ["num_features desc"];
    query.outStatistics = [
      {
        onStatisticField: "capacity_mw",
        outStatisticFieldName: "capacity_total",
        statisticType: "sum"
      },
      {
        onStatisticField: "1",
        outStatisticFieldName: "num_features",
        statisticType: "count"
      },
      {
        onStatisticField: "capacity_mw",
        outStatisticFieldName: "capacity_max",
        statisticType: "max"
      }
    ];

    const { features } = await layerView.queryFeatures(query);
    const stats = features.map((feature) => feature.attributes);

    let table = `
  <div class="table-container">
    <span style="font-size: 14pt"><strong>Summary by fuel type</strong></span>
    <br/>
    <br/>
    <table class="esri-widget popup">
      <tr class="head"><td>Fuel</td><td>Count</td><td>Capacity (mW)</td><td>Largest plant (mW)</td></tr>
`;

    let totalCapacity = 0;
    let totalCount = 0;

    stats.forEach((stat) => {
      const fuel = stat.fuel1;
      const total = stat.capacity_total;
      const max = stat.capacity_max;
      const count = stat.num_features;

      totalCapacity += total;
      totalCount += count;

      table += `
    <tr><td><span style:'font-weight:bolder'>${fuel}</span></td><td class="num">${count}</td><td class="num">${roundDecimals(
        total,
        2
      ).toLocaleString()}</td><td class="num">${roundDecimals(
        max,
        2
      ).toLocaleString()}</td></tr>
  `;
    });

    table += `
  </table>
</div>`;

    view.popup.content =
      `
  <div style="font-size: 12pt">
  Number of features: <strong>${totalCount.toLocaleString()}</strong><br>
  Total capacity (mW): <strong>${roundDecimals(
    totalCapacity,
    2
  ).toLocaleString()}</strong><br>
  </div><br>
` + table;
  }

  function processParams(graphic, layerView) {
    if (!graphic || !layerView) {
      throw new Error("Graphic or layerView not provided.");
    }

    if (!graphic.isAggregate) {
      throw new Error("Graphic must represent a cluster.");
    }
  }

  function roundDecimals(num, places) {
    return Math.round(num * Math.pow(10, places)) / Math.pow(10, places);
  }
});