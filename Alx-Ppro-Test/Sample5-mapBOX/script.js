mapboxgl.accessToken = 'pk.eyJ1Ijoib3RvbWlzaW4iLCJhIjoiY2xrODkxN3JxMGNxYzNudDViYnQ5N2NiNCJ9.5U9_Jt9Ztk_LxxSAiotYTA';

const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/light-v10',
    center: [-10, 10], // Centered on West Africa
    zoom: 3
});

// Dummy GeoJSON data
L.geojson(ngaAdmin).addTo(map)
const geojson = {
    type: 'FeatureCollection',
    features: [
        // Add your GeoJSON features here
    ]
};

map.on('load', () => {
    // Add GeoJSON data to the map
    map.addSource('points', {
        type: 'geojson',
        data: geojson
    });

    map.addLayer({
        id: 'points',
        type: 'circle',
        source: 'points',
        paint: {
            'circle-radius': 6,
            'circle-color': '#007BFF'
        }
    });
});

// Chart.js
const ctx = document.getElementById('chart').getContext('2d');
const data = {
    labels: ['Roads', 'Floods', 'Insecurity', 'Crime', 'Drought '],
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
    data: data
});

// Sign-up form
const signupForm = document.getElementById('signup-form');
signupForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const emailInput = document.getElementById('email-input').value;
    // Handle the sign-up process here
});
