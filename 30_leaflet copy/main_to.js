console.log("It's fine")
window.onload = init;  // help windows to only run after the HTML script has finished running

function init(){
  const mapElement = document.getElementById('mapid')

  const openstreetMapStandard = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    noWrap:true,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  });

  const stadiaMaps = L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors' 
  })

// leaftletBase Map
  const mymap = L.map(mapElement, {
    center:[-37.109955444643475, 129.41894531250003], // define the center when loaded/reloaded
    zoom: 4, // define the zoom level
    miniZoom: 4, // define the minimum zoom level
    zoomSnap:0.25, // Forces the zoom level 
    zoonDelta: 0.25, // Forces the zoom level
    layers: [stadiaMaps], // define a base, this can be changed to openstreetMapStandard
    worldCopyJump: true,
  })

 // Basemap object
  const baseLayers = {
    '<b>openstreetMapStandard</b>': openstreetMapStandard,
    'stadiaMaps': stadiaMaps
  }

  //Raster file overlay
  const perthBaseMapimage = './data/raster_file.png'; //raster file source
  const perthBaseMapbounds = [[-37.109955444643475, 129.41894531250003], [-26.295877391487554,141.06445312500003]] // define the map boundary
  const imageperthOverlay = L.imageOverlay(perthBaseMapimage, perthBaseMapbounds).addTo(mymap) 

  // overlayer object
  const overlaysLayers = {
    'Perth image': imageperthOverlay
  }

 // Click event for getting the lat and long
  mymap.on('click', function(event){
    console.log(event.latlng) // define an event function that outputs a lat and long when clicked
  })

  //Map layer control
  const layerControl = L.control.layers(baseLayers,overlaysLayers,{},{
    collapsed:false, // set the behaviour not to collapse
    position: 'topleft' //set the postion of the control
  }).addTo(mymap);

  // Add a perth city marker
  const perthMarker = L.marker([-32.27087780256757, 116.05957031250001], {
    title: 'Perth City',
    opacity: 0.5
  }).addTo(mymap)

  // perthMarker pop up
  const perthMarkerPopup = perthMarker.bindPopup('Perth city for pop up');
  perth

  // Geolocation API

  mymap.locate({setView:true, maxZoom: 18})
    var radius = e.accuracy.toFixed(2);
    var locationMarker = L.marker(e.latlong).addTo(mymap)
    .bindPopup('You are within ' + radius + ' meters from this point');
    var locationCirlce = L.circle(elaing, radius).addTo(mymap)
  mymap.on('locationfound', onLocationFound);

  // Distance calculator
  mymap.on('click', function(e){
    let latlng = e.latlng;
    L.marker(latlng)
    .addTo(mymap) 
  })
}