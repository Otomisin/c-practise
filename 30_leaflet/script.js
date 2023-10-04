// Map initialization 
var map = L.map('map').setView([28.3949, 84.1240], 8);

/*==============================================
            TILE LAYER and WMS
===============================================*/
//osm layer
var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});
osm.addTo(map);

// watercolor 
var watercolor = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    subdomains: 'abcd',
    minZoom: 1,
    maxZoom: 16,
    ext: 'jpg'
});

// dark map 
var dark = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 19
});

// google street 
googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
});

//google satellite
googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
});

var wms = L.tileLayer.wms("http://localhost:8080/geoserver/wms", {
    layers: 'geoapp:admin',
    format: 'image/png',
    transparent: true,
    attribution: "wms test"
});

/*==============================================
                MARKER
===============================================*/
var myIcon = L.icon({
    iconUrl: 'img/red_marker.png',
    iconSize: [40, 40],
});

var singleMarker = L.marker([28.3949, 84.1240], { icon: myIcon, draggable: true });
var popup = singleMarker.bindPopup('This is Nepal. ' + singleMarker.getLatLng()).openPopup();
popup.addTo(map);

var secondMarker = L.marker([29.3949, 83.1240], { icon: myIcon, draggable: true });

console.log(singleMarker.toGeoJSON());

/*==============================================
            GEOJSON
===============================================*/
var pointData = L.geoJSON(pointJson).addTo(map);
var lineData = L.geoJSON(lineJson).addTo(map);
var lineData = L.geoJSON(ngaAdmin).addTo(map);
var polygonData = L.geoJSON(polygonJson, {
    onEachFeature: function (feature, layer) {
        layer.bindPopup(`<b>Name: </b>` + feature.properties.name);
    },
    style: {
        fillColor: 'red',
        fillOpacity: 1,
        color: '#c0c0c0',
    }
}).addTo(map);

/*==============================================
        LAYER CONTROL
===============================================*/
var baseMaps = {
    "OSM": osm,
    "Water color map": watercolor,
    'Dark': dark,
    'Google Street': googleStreets,
    "Google Satellite": googleSat,
};
var overlayMaps = {
    "First Marker": singleMarker,
    'Second Marker': secondMarker,
    'Point Data': pointData,
    'Line Data': lineData,
    'Polygon Data': polygonData,
    'wms': wms
};

L.control.layers(baseMaps, overlayMaps, { collapsed: false }).addTo(map);

/*==============================================
        LEAFLET EVENTS
===============================================*/
map.on('mouseover', function () {
    console.log('Your mouse is over the map');
});

map.on('mousemove', function (e) {
    document.getElementsByClassName('coordinate')[0].innerHTML = 'lat: ' + e.latlng.lat + 'lng: ' + e.latlng.lng;
    console.log('lat: ' + e.latlng.lat, 'lng: ' + e.latlng.lng);
});

/*==============================================
        STYLE CUSTOMIZATION
===============================================*/