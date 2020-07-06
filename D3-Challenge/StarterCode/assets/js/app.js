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
	.select("#scatter")
	.append("svg")
	.attr("height", svgHeight)
	.attr("width", svgWidth)
	.append("g")
	.attr("transform", `translate(${margin.left}, ${margin.top})`);;

d3.csv("./assets/data/data.csv").then(function(data){

	data.forEach(function(data){
		healthCare.push(+data.healthcare);
	});
	data.forEach(function(data){
		pov.push(+data.poverty);
	});
	
	var x = d3.scaleLinear()
		.domain([0, d3.max(pov) + 5])
		.range([0, width]);
	svg.append("g")
		.attr("transform", "translate(0, " + height + ")")
		.call(d3.axisBottom(x));

	var y = d3.scaleLinear()
		.domain([d3.max(healthCare) + 5, 0])
		.range([height, 0]);
	svg.append("g")
		.call(d3.axisLeft(y));

	svg.append('g')
		.selectAll("dot")
		.data(data)
		.enter()
		.append("circle")
			.attr("cx", 5.0)
			.attr("cy", 5.0)
			.attr("r", 5)
			.style("fill", "#69b3a2")
});

console.log(healthCare);
console.log(pov);

