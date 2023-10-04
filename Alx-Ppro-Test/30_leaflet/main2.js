window.onload = init;

function init() {
  // HTML element
  const mapElement = document.getElementById('mapid')

  // Basemaps
  const openStreetMapStandard = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    noWrap: true,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  });

  const stadiaMaps = L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
  })

  // Leaflet map object
  const mymap = L.map(mapElement, {
    center: [9.27, 8.299],
    zoom: 6.5,
    minZoom: 1,
    zoomSnap: 0.25,
    zoomDelta: 0.25,
    easeLinearity: 0.2,
    worldCopyJump: true,
    layers: [openStreetMapStandard] 
  })

  // Basemap Object
  const baseLayers = {
    '<b>OpenStreetMapStandard</b>': openStreetMapStandard,
    'StadiaMaps': stadiaMaps
  }

  // Layer control
  const layerControl = L.control.layers(baseLayers, overlayerLayers, {
    collapsed: false,
    position: 'topright'
  }).addTo(mymap)

  // Perth marker
  const perthMarker = L.marker([-32.01791974628008, 115.89434607367286], {
    opacity: 1
  }).addTo(mymap)

  const perthMarkerPopup = perthMarker.bindPopup('Perth city from the popup');
  const perthMarkerTooltip = perthMarker.bindTooltip("Perth city from the tooltip").openTooltip();

  // Geolocation API
  mymap.locate({setView:true, maxZoom: 18})

  function onLocationFound(e) {
    var radius = e.accuracy.toFixed(2);

    var locationMarker = L.marker(e.latlng).addTo(mymap)
      .bindPopup('You are within ' + radius  + ' metres from this point').openPopup()

    var locationCircle = L.circle(e.latlng, radius).addTo(mymap);
  }

  mymap.on('locationfound', onLocationFound);

  function onLocationError(e) {
    window.alert(e.message)
  }
  mymap.on('locationerror', onLocationError);

  // Distance calculation demo
  const myCustomIcon = L.icon({
    iconUrl: './data/icons8-location-80.png',
    iconSize: [30, 30],
    iconAnchor: [15, 46],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]    
  });

  var counter = 0
  var coordinates = []

  mymap.on('click', function(e) {
    counter += 1;
    let latlng = e.latlng;
    coordinates.push(latlng)

    let popup = L.popup({
      autoClose: false,
      closeOnClick: false
    }).setContent(String(counter))

    L.marker(latlng, {icon: myCustomIcon})
      .addTo(mymap)
      .bindPopup(popup)
      .openPopup()

    if (counter >= 2) {
      let distance = mymap.distance(coordinates[0], coordinates[1])
      console.log(distance)
      coordinates.shift()
    }
  })
}

// Chart.js code (as shown in the previous response)
const ctx = document.getElementById('chart').getContext('2d');
const data = {
  labels: ['Roads', 'Floods', 'Insecurity', 'Crime', 'Drought'],
  datasets: [{
    data: [12, 19, 3, 17, 28],
    backgroundColor: [
      '#007BFF',
      '#FFC107',
      '#28A745',
      '#DC3545',
      '#17A2B8'
    ]
  }]
};

const chart = new Chart(ctx, {
  type: 'pie',
  data: data,
  options: {
    responsive: true,
    maintainAspectRatio: false, // Allows you to control the aspect ratio
    width: 50, // Adjust the width of the chart as needed
    height: 200, // Adjust the height of the chart as needed
  }
});