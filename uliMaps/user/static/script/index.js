var map = L.map('map').setView([4.805178, -75.760217], 15);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


function showLocation(){
    var marker = L.marker([4.806218, -75.760584]).addTo(map);
}