// @TODO: YOUR CODE HERE!
var healthCare =[];
var pov = [];

var svgWidth = window.innerWidth;
var svgHeight = window.innerHeight;

var margin = {
	top: 50,
	right: 50,
	bottom: 50,
	left: 50
};

var height = svgHeight - margin.top - margin.bottom;
var width = svgWidth - margin.left - margin.right;

var svg = d3
	.select("body")
	.append("svg")
	.attr("height", svgHeight)
	.attr("width", svgWidth);

var chartGroup = svg.append("g")
	.attr("transform", `translate(${margin.left}, ${margin.top})`);




d3.csv("./assets/data/data.csv").then(function(data){
	console.log(data);

	data.forEach(function(data){
		healthCare.push(data.healthcare);
	});
	data.forEach(function(data){
		pov.push(data.poverty);
	});
	
});

console.log(healthCare);
console.log(pov);

