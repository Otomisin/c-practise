require([
  "esri/views/MapView",
  "esri/WebMap",
  "esri/widgets/Legend",
  "esri/widgets/Expand",
  "esri/widgets/Bookmarks",
  "esri/smartMapping/labels/clusters",
  "esri/core/lang",
  "esri/core/promiseUtils",
  "esri/core/watchUtils",
  "esri/geometry/geometryEngine"
], function (
  MapView,
  WebMap,
  Legend,
  Expand,
  Bookmarks,
  clusterLabelCreator,
  lang,
  promiseUtils,
  watchUtils,
  geometryEngine
) {
  // declare chart variables to update as the user interacts with the sample

  let yearChart,
    ageChart,
    dispositionChart,
    genderChart,
    raceChart,
    totalNumber,
    avgAge,
    avgOpenTime;

  // load a web map containing homicide statistics
  // from a portal item

  const webmap = new WebMap({
    portalItem: {
      id: "96cf806c32874026bef5f586315f098c"
    }
  });

  const view = new MapView({
    map: webmap,
    container: "viewDiv",
    constraints: {
      minScale: 300000
    },
    highlightOptions: {
      color: "black",
      haloOpacity: 0.65,
      fillOpacity: 0.45
    }
  });

  // Add UI elements to the view

  // Displays instructions to the user for understanding the sample
  // And places them in an Expand widget instance

  const titleContent = document.createElement("div");
  titleContent.style.padding = "15px";
  titleContent.style.backgroundColor = "white";
  titleContent.style.width = "500px";
  titleContent.innerHTML = [
    "<div id='title' class='esri-widget'>",
    "<span id='num-homicides'>0</span> homicides occurred in this area over from 2008-2018.",
    "The average age of the victims is <span id='avg-age'>0</span>. The average time an unsolved case has been",
    "open is <span id='avg-open-time'>0</span> years.",
    "</div>"
  ].join(" ");

  const titleExpand = new Expand({
    expandIconClass: "esri-icon-dashboard",
    expandTooltip: "Summary stats",
    view: view,
    content: titleContent,
    expanded: view.widthBreakpoint !== "xsmall"
  });
  view.ui.add(titleExpand, "top-right");

  const legendExpand = new Expand({
    view: view,
    content: new Legend({
      view: view
    }),
    expanded: view.widthBreakpoint !== "xsmall"
  });
  view.ui.add(legendExpand, "bottom-left");

  view.watch("widthBreakpoint", function (newValue) {
    titleExpand.expanded = newValue !== "xsmall";
    legendExpand.expanded = newValue !== "xsmall";
  });

  const bookmarksWidget = new Bookmarks({
    view: view
  });

  const bookmarksExpand = new Expand({
    view: view,
    content: bookmarksWidget
  });
  view.ui.add(bookmarksExpand, "top-right");

  bookmarksWidget.on("select-bookmark", function (event) {
    bookmarksExpand.expanded = false;
  });

  // Displays instructions to the user for understanding the sample
  // And places them in an Expand widget instance

  const sampleInstructions = document.createElement("div");
  sampleInstructions.style.padding = "10px";
  sampleInstructions.style.backgroundColor = "white";
  sampleInstructions.style.width = "300px";
  sampleInstructions.innerHTML = [
    "<b>Touch or click</b> a cluster to view stats",
    "for features included in the cluster."
  ].join(" ");

  const instructionsExpand = new Expand({
    expandIconClass: "esri-icon-question",
    expandTooltip: "How to use this sample",
    view: view,
    content: sampleInstructions
  });
  view.ui.add(instructionsExpand, "top-left");

  let highlightHandle = null;

  /**
   * Create charts and start querying the layer view when
   * the view is ready and data begins to draw in the view
   */
  view.when().then(async function () {
    // Create the charts when the view is ready
    createCharts();

    const layer = webmap.layers.getItemAt(0);

    // generates default labelingInfo
    const { labelingInfo, clusterMinSize } = await clusterLabelCreator
      .getLabelSchemes({
        layer,
        view
      })
      .then((labelSchemes) => labelSchemes.primaryScheme);

    layer.featureReduction = {
      type: "cluster",
      labelingInfo,
      clusterMinSize
    };

    layer.outFields = [
      "victim_age_years",
      "victim_race",
      "victim_sex",
      "reported_year",
      "disposition",
      "milliseconds"
    ];

    view.whenLayerView(layer).then(function (layerView) {
      watchUtils.whenFalseOnce(layerView, "updating", function (val) {
        // Query layer view statistics as the user clicks
        view.on(["click"], async (event) => {
          event.stopPropagation();
          const hitResponse = await view.hitTest(event, { include: layer });

          if (hitResponse.results.length > 0) {
            const graphic = hitResponse.results[0].graphic;

            if (graphic.isAggregate) {
              await queryStatsOnDrag(layerView, event, graphic.getObjectId())
                .then(updateCharts)
                .catch(function (error) {
                  if (error.name !== "AbortError") {
                    console.error(error);
                  }
                });
            } else {
              if (highlightHandle) {
                highlightHandle.remove();
              }
              // Add a highlight to the clicked feature
              highlightHandle = layerView.highlight([graphic.getObjectId()]);
              // set the objectId of the selected
              // cluster to null to avoid its inclusion
              // in cluster queries

              layer.featureReduction = {
                type: "cluster",
                labelingInfo,
                clusterMinSize,
                excludedLabels: [graphic.getAttribute("cluster_label")]
              };

              await queryStatsOnDrag(layerView, event, null)
                .then(updateCharts)
                .catch(function (error) {
                  if (error.name !== "AbortError") {
                    console.error(error);
                  }
                });

              layer.featureReduction = {
                type: "cluster",
                labelingInfo,
                clusterMinSize
              };
            }
          }
        });
      });
    });

    function createCharts() {
      const chartsContainer = document.getElementById("panel");
      const chartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: [
            {
              stacked: true,
              scaleLabel: {
                display: true,
                labelString: "Year"
              }
            }
          ],
          y: [
            {
              stacked: true,
              ticks: {
                beginAtZero: true,
                precision: 0
              }
            }
          ]
        }
      };

      // Chart for number of homicides per year
      const yearCtx = document.getElementById("year-chart").getContext("2d");
      yearChart = new Chart(yearCtx, {
        type: "bar",
        data: {
          datasets: []
        },
        options: {
          ...chartOptions,
          plugins: {
            tooltip: {
              mode: "index",
              intersect: false
            },
            legend: {
              display: true,
              position: "bottom"
            }
          }
        }
      });

      // Chart for victim age distribution
      const ageCtx = document.getElementById("age-chart").getContext("2d");
      ageChart = new Chart(ageCtx, {
        type: "bar",
        data: {
          datasets: []
        },
        options: {
          ...chartOptions,
          plugins: {
            tooltip: {
              mode: "index",
              intersect: false
            },
            legend: {
              display: true,
              position: "bottom"
            }
          }
        }
      });

      // Chart for disposition of cases
      const dispositionCtx = document
        .getElementById("disposition-chart")
        .getContext("2d");
      dispositionChart = new Chart(dispositionCtx, {
        type: "doughnut",
        data: {
          datasets: [
            {
              data: [],
              backgroundColor: [
                "#FF6384",
                "#36A2EB",
                "#FFCE56",
                "#2ecc71",
                "#3498db",
                "#9b59b6",
                "#e74c3c"
              ]
            }
          ],
          labels: []
        },
        options: {
          ...chartOptions,
          plugins: {
            legend: {
              position: "right"
            }
          }
        }
      });

      // Chart for gender of victims
      const genderCtx = document.getElementById("gender-chart").getContext("2d");
      genderChart = new Chart(genderCtx, {
        type: "doughnut",
        data: {
          datasets: [
            {
              data: [],
              backgroundColor: ["#FF6384", "#36A2EB"]
            }
          ],
          labels: []
        },
        options: {
          ...chartOptions,
          plugins: {
            legend: {
              position: "right"
            }
          }
        }
      });

      // Chart for race of victims
      const raceCtx = document.getElementById("race-chart").getContext("2d");
      raceChart = new Chart(raceCtx, {
        type: "doughnut",
        data: {
          datasets: [
            {
              data: [],
              backgroundColor: [
                "#FF6384",
                "#36A2EB",
                "#FFCE56",
                "#2ecc71",
                "#3498db",
                "#9b59b6",
                "#e74c3c",
                "#34495e"
              ]
            }
          ],
          labels: []
        },
        options: {
          ...chartOptions,
          plugins: {
            legend: {
              position: "right"
            }
          }
        }
      });
    }

    function updateCharts() {
      yearChart.data.datasets = [];
      ageChart.data.datasets = [];
      dispositionChart.data.datasets = [];
      genderChart.data.datasets = [];
      raceChart.data.datasets = [];

      // Query statistics for each year
      layer.queryFeatures({
        where: "1=1",
        returnGeometry: false,
        outStatistics: [
          {
            onStatisticField: "reported_year",
            outStatisticFieldName: "year",
            statisticType: "count"
          },
          {
            onStatisticField: "victim_age_years",
            outStatisticFieldName: "avg_age",
            statisticType: "avg"
          },
          {
            onStatisticField: "milliseconds",
            outStatisticFieldName: "avg_open_time",
            statisticType: "avg"
          }
        ],
        groupByFieldsForStatistics: ["reported_year"]
      }).then(function (response) {
        const yearData = response.features.map(function (feature) {
          return {
            year: feature.attributes.year,
            count: feature.attributes.count,
            avg_age: feature.attributes.avg_age,
            avg_open_time: feature.attributes.avg_open_time / 31536000000 // milliseconds to years
          };
        });

        yearData.sort((a, b) => a.year - b.year);

        yearChart.data.labels = yearData.map((data) => data.year);
        yearChart.options.scales.y[0].stacked = true;
        yearChart.data.datasets.push({
          label: "Homicides by Year",
          data: yearData.map((data) => data.count),
          backgroundColor: "rgba(255, 99, 132, 0.6)"
        });

        avgAge = yearData.reduce((acc, data) => acc + data.avg_age, 0) / yearData.length;
        avgOpenTime = yearData.reduce((acc, data) => acc + data.avg_open_time, 0) / yearData.length;

        document.getElementById("avg-age").textContent = avgAge.toFixed(2);
        document.getElementById("avg-open-time").textContent = avgOpenTime.toFixed(2);
      });

      // Query statistics for age distribution
      layer.queryFeatures({
        where: "1=1",
        returnGeometry: false,
        outStatistics: [
          {
            onStatisticField: "victim_age_years",
            outStatisticFieldName: "age",
            statisticType: "count"
          }
        ],
        groupByFieldsForStatistics: ["victim_age_years"]
      }).then(function (response) {
        const ageData = response.features.map(function (feature) {
          return {
            age: feature.attributes.victim_age_years,
            count: feature.attributes.age
          };
        });

        ageData.sort((a, b) => a.age - b.age);

        ageChart.data.labels = ageData.map((data) => data.age);
        ageChart.data.datasets.push({
          label: "Age Distribution",
          data: ageData.map((data) => data.count),
          backgroundColor: "rgba(54, 162, 235, 0.6)"
        });
      });

      // Query statistics for disposition
      layer.queryFeatures({
        where: "1=1",
        returnGeometry: false,
        outStatistics: [
          {
            onStatisticField: "disposition",
            outStatisticFieldName: "disposition",
            statisticType: "count"
          }
        ],
        groupByFieldsForStatistics: ["disposition"]
      }).then(function (response) {
        const dispositionData = response.features.map(function (feature) {
          return {
            disposition: feature.attributes.disposition,
            count: feature.attributes.disposition
          };
        });

        dispositionData.sort((a, b) => a.disposition.localeCompare(b.disposition));

        dispositionChart.data.labels = dispositionData.map((data) => data.disposition);
        dispositionChart.data.datasets.push({
          data: dispositionData.map((data) => data.count)
        });
      });

      // Query statistics for gender
      layer.queryFeatures({
        where: "1=1",
        returnGeometry: false,
        outStatistics: [
          {
            onStatisticField: "victim_sex",
            outStatisticFieldName: "sex",
            statisticType: "count"
          }
        ],
        groupByFieldsForStatistics: ["victim_sex"]
      }).then(function (response) {
        const genderData = response.features.map(function (feature) {
          return {
            sex: feature.attributes.victim_sex,
            count: feature.attributes.sex
          };
        });

        genderData.sort((a, b) => a.sex.localeCompare(b.sex));

        genderChart.data.labels = genderData.map((data) => data.sex);
        genderChart.data.datasets.push({
          data: genderData.map((data) => data.count)
        });
      });

      // Query statistics for race
      layer.queryFeatures({
        where: "1=1",
        returnGeometry: false,
        outStatistics: [
          {
            onStatisticField: "victim_race",
            outStatisticFieldName: "race",
            statisticType: "count"
          }
        ],
        groupByFieldsForStatistics: ["victim_race"]
      }).then(function (response) {
        const raceData = response.features.map(function (feature) {
          return {
            race: feature.attributes.victim_race,
            count: feature.attributes.race
          };
        });

        raceData.sort((a, b) => a.race.localeCompare(b.race));

        raceChart.data.labels = raceData.map((data) => data.race);
        raceChart.data.datasets.push({
          data: raceData.map((data) => data.count)
        });
      });

      // Update the charts
      yearChart.update();
      ageChart.update();
      dispositionChart.update();
      genderChart.update();
      raceChart.update();
    }

    /**
     * Query the layer view to fetch the statistics for a cluster
     * or individual feature
     * @param {module:esri/views/layers/support/FeatureLayerView} layerView
     * @param {Object} event
     * @param {Number} objectId
     * @returns {Promise<Array>} promises
     */
    async function queryStatsOnDrag(layerView, event, objectId) {
      // Promises to fetch data from the layer
      const promises = [];

      // query for the stats
      promises.push(
        promiseUtils.create(function (resolve) {
          // Container for promises created in the loop
          const promises = [];
          const stats = [];
          const latlngs = [];
          const layer = webmap.layers.getItemAt(0);

          // Create a default popup template for the stats
          const template = {
            title: "Homicides",
            content: createDefaultPopupContent(stats, latlngs),
            fieldInfos: [
              {
                fieldName: "reported_year",
                label: "Year"
              },
              {
                fieldName: "victim_age_years",
                label: "Age"
              },
              {
                fieldName: "victim_race",
                label: "Race"
              },
              {
                fieldName: "victim_sex",
                label: "Gender"
              },
              {
                fieldName: "disposition",
                label: "Disposition"
              }
            ]
          };

          // Execute a query against the layer view and resolve the promise with the results
          layerView.queryFeatures().then(function (response) {
            const queryStats = response.features.map(function (feature) {
              return {
                reported_year: feature.attributes.reported_year,
                victim_age_years: feature.attributes.victim_age_years,
                victim_race: feature.attributes.victim_race,
                victim_sex: feature.attributes.victim_sex,
                disposition: feature.attributes.disposition
              };
            });

            // Add latlngs for the popup
            latlngs.push(event.mapPoint);

            // If objectId is specified, we are querying a cluster, so we don't add
            // the cluster's stats to the stats list
            if (objectId) {
              resolve({ stats, latlngs });
            } else {
              stats.push(...queryStats);
              resolve({ stats, latlngs });
            }
          });
        })
      );

      // Check for other resolved promises
      const resolvedPromises = await Promise.all(promises);
      let stats = [];
      let latlngs = [];

      // Combine the resolved promises
      resolvedPromises.forEach(function (promise) {
        stats = stats.concat(promise.stats);
        latlngs = latlngs.concat(promise.latlngs);
      });

      // Show the data in the charts and popup
      updateCharts(stats);
      view.popup.open({
        features: [
          {
            geometry: event.mapPoint,
            attributes: {
              latlngs: latlngs,
              stats: stats
            }
          }
        ],
        location: event.mapPoint,
        updateLocationEnabled: true
      });
    }

    // Create a default popup template for the statistics
    function createDefaultPopupContent(stats, latlngs) {
      // Get the content div
      const div = document.createElement("div");
      div.classList.add("esri-feature");

      // Add stats to the content
      stats.forEach(function (stat) {
        const statDiv = document.createElement("div");
        statDiv.classList.add("stats-container");
        statDiv.innerHTML = `
          <span class="stats-label">Year:</span>
          <span class="stats-value">${stat.reported_year}</span><br>
          <span class="stats-label">Age:</span>
          <span class="stats-value">${stat.victim_age_years}</span><br>
          <span class="stats-label">Race:</span>
          <span class="stats-value">${stat.victim_race}</span><br>
          <span class="stats-label">Gender:</span>
          <span class="stats-value">${stat.victim_sex}</span><br>
          <span class="stats-label">Disposition:</span>
          <span class="stats-value">${stat.disposition}</span><br>
        `;

        // Add latlngs for the popup
        const latlngIndex = stats.indexOf(stat);
        const latlng = latlngs[latlngIndex];

        statDiv.addEventListener("click", function () {
          view.popup.open({
            title: "Details",
            location: latlng,
            content: div
          });
        });

        // Append the div to the content
        div.appendChild(statDiv);
      });

      return div;
    }
  });
});
