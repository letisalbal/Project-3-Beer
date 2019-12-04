//Brewery Location Pie Chart
var trace = {
    labels: ["brewerypub", "large", "micro"],
    values: [7, 1, 12],
    type: 'pie'
  };
  
  var data = [trace];
  
  var layout = {
    title: "Brewery Locations in NY",
    xaxis: { title: "Brewery Type"},
    yaxis: { title: "Count"}
  };
  
  Plotly.newPlot("plot3", data, layout);