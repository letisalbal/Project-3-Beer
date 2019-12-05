//Brewery State Location Bar Chart
var trace1 = {
    x: ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS",
        "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA",
        "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"],
    y: [7, 3, 2, 11, 39, 47, 8, 1, 2, 15, 7, 4, 5, 5, 18, 22,
        3, 4, 5, 23, 7, 9, 32, 12, 9, 2, 9, 19, 1, 5, 3, 3, 4, 2, 16,
        15, 6, 29, 25, 5, 4, 1, 3, 28, 4, 16, 10, 23, 20, 1, 4],
    type: 'bar',
    marker: {color: 'orange'}
};

var data = [trace1];

var layout = {
    title: "Brewery Locations in the United States",
    xaxis: { title: "States" },
    yaxis: { title: "Count" }

};

Plotly.newPlot("plot4", data, layout);