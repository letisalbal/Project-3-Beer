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
  

// Beer Style Bar Chart
// Create the Traces
var trace1 = {
  x: data.beer_style,
  y: data.average_ibu,
  mode: "markers",
  type: "scatter",
  name: "IBU",
  marker: {
    color: "#2077b4",
    symbol: "hexagram"
  }
};

var trace2 = {
  x: data.beer_style,
  y: data.average_abv,
  mode: "markers",
  type: "scatter",
  name: "ABV",
  marker: {
    color: "orange",
    symbol: "diamond-x"
  }
};

var trace3 = {
  x: data.beer_style,
  y: data.average_srm,
  mode: "markers",
  type: "scatter",
  name: "SRM",
  marker: {
    color: "rgba(156, 165, 196, 1.0)",
    symbol: "cross"
  }
};
var trace4 = {
  x: data.beer_style,
  y: data.average_og,
  mode: "markers",
  type: "scatter",
  name: "OG",
  marker: {
    color: "blue",
    symbol: "triangle"
  }
};

var trace5 = {
  x: data.beer_style,
  y: data.average_fg,
  mode: "markers",
  type: "scatter",
  name: "FG",
  marker: {
    color: "green",
    symbol: "circle"
  }
};

// Create the data array for the plot
var data = [trace1, trace2, trace3, trace4, trace5];

// Define the plot layout
var layout = {
  title: "Characteristics in Beer Style",
  xaxis: { title: "Beer Style" },
  yaxis: { title: "Count of Characteristics" }
};

// Plot the chart to a div tag with id "plot"
Plotly.newPlot("plot2", data, layout);
