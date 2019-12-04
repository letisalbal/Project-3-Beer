//Brewery Location Pie Chart
var trace = {
    x: ["brewerypub", "large", "micro"],
    y: [7, 1, 12],
    type: 'bar'
  };
  
  var data = [trace];
  
  var layout = {
    title: "Brewery Locations in NY",
    xaxis: { title: "Brewery Type"},
    yaxis: { title: "Count"}

  };
  
  Plotly.newPlot("plot3", data, layout);