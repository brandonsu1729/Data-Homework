var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: '© <a href="https://www.mapbox.com/about/maps/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>',
tileSize: 512,
maxZoom: 18,
zoomOffset: -1,
id: 'mapbox/streets-v11',
accessToken: 'pk.eyJ1IjoiYnJhbmRvbnN1MTcyOSIsImEiOiJja2MxOW9sMnoxYzZtMnh1NmloenhjeGJlIn0.tyWpIzFrDUUavXdzBsCbFQ'
}).addTo(myMap);


var link = "significant_month.geojson"
var heatArray = [];
d3.json(link, function(data){

	for (var i = 0; i < data.features.length; i++){
		var location = data.features[i].geometry.coordinates;

		heatArray.push([location[1], location[0]]);
		/*L.marker([data.features[i].geometry.coordinates[1], 
			data.features[i].geometry.coordinates[0]],{
			title: data.features[i].properties.place}).addTo(myMap);*/
}})

var heat = L.heatLayer(heatArray, {
	radius: 50,
	blur: 0
}).addTo(myMap)