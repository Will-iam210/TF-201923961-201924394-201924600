(async function() {
	console.log("Toda la alegría del mundo.");

	// Data

	const urlgraph = "graph";
	const urlpaths = "paths"
	const graph    = await d3.json(urlgraph);
	const paths    = await d3.json(urlpaths);

	// config

	const margin = {
		top:    10,
		right:  10,
		bottom: 10,
		left:   10
	};
	const box    = {
		width:   990,
		height:  695,
		bwidth:  990 - margin.left - margin.right,
	  bheight: 695 - margin.top - margin.bottom
	};

	// Canvas y elementos

	const svg = d3
		.select("#box")
		.append("svg")
		.attr("width", box.width)
		.attr("height", box.height);

	const g = svg.append("g")
		.attr("transform", `translate(${margin.left}, ${margin.top})`);

	const [lon, lat] = [d => d[0], d => d[1]];

	const lineGenerator = d3.line().x(lon).y(lat);

	const line2 = g.append("path")
		.attr("d", lineGenerator(paths.path1))
		.attr("fill", "none")
		.attr("stroke", "#273043")
		.attr("stroke-width", 1.5)
		.attr("opacity", 1);

	const line3 = g.append("path")
		.attr("d", lineGenerator(paths.path2))
		.attr("fill", "none")
		.attr("stroke", "#E83151")
		.attr("stroke-width", 1)
		.attr("opacity", 1);

	const line = g.append("path")
		.attr("d", lineGenerator(paths.bestpath))
		.attr("fill", "none")
		.attr("stroke", "#F5A65B")
		.attr("stroke-width", 0.5)
		.attr("opacity", 1);

	const dots = g.selectAll("circle")
		.data(graph.loc)
		.enter()
		.append("circle")
		.attr("cx", lon)
		.attr("cy", lat)
		.attr("r", 2.0)
		.attr("fill", "Black")
		.attr("opacity", 1);

	// Funciones y eventos

	// Empezamos

})();

/* vim: set tabstop=2:softtabstop=2:shiftwidth=2:noexpandtab */

