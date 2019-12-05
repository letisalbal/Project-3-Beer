//Brewery NYS Location Bar Chart
var trace = {
    x: ["Brewery Pub", "Large", "Micro"],
    y: [7, 1, 12],
    type: 'bar',
  };
  
  var data = [trace];
  
  var layout = {
    title: "Brewery Locations in NY",
    xaxis: { title: "Brewery Type"},
    yaxis: { title: "Count"}

  };
  
  Plotly.newPlot("plot3", data, layout);