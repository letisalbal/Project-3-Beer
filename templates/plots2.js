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
      color: "yellow",
      symbol: "square"
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
    title: {
      text: "Characteristics in Beer Style",
      font: {
        size: 24
      },
    }, 
    xaxis: { 
      title: {
        text: "Beer Style", 
        font: {
          size: 20
        }
      },
    },
    yaxis: { 
      title: {
        text: "Count", 
        font: {
          size: 20
        }
      }
    }
  };
  
  // Plot the chart to a div tag with id "plot"
  Plotly.newPlot("plot2", data, layout);
  