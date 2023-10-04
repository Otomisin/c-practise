// script.js

const map = L.map('map').setView([10, -10], 3); // Centered on West Africa
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Dummy GeoJSON data
const geojson = {
    type: 'FeatureCollection',
    features: [
        // Add your GeoJSON features here
    ]
};

L.geoJSON(geojson, {
    pointToLayer: function (feature, latlng) {
        return L.circleMarker(latlng, {
            radius: 6,
            fillColor: '#007BFF',
            color: '#000',
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
        });
    }
}).addTo(map);

// Chart.js
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
    data: data
});

// Sign-up form
const signupForm = document.getElementById('signup-form');
signupForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const emailInput = document.getElementById('email-input').value;
    // Handle the sign-up process here
});
