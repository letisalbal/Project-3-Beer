var data = [{
  type: 'scattergeo',
  mode: 'markers+text',
  text: [
    'Adirondack Toboggan Company Microbrewery', 'Black Forest Brew Haus', 'Blue Point Brewing Co', 
    'Browns Brewing Co', 'Careys Brew House', 'Copper City Brewing Company',
     'Diversion Brewing Co', 'Empire Brewing Co', 'Erie Canal Brewing Company',
    'Fairport Brewing Co', 'Flying Bison Brewing Co', 'Glenmere Brewing Co',
     'Greenport Harbor Brewing Co, LLC','Gun Hill Brewing Co','Irish Mafia Brewing Co',
    'Lafayette Brewing Co','Lost Kingdom Brewery','Peacemaker Brewing Company',
    'Pressure Drop Brewing', 'Rohrbachs Railroad St Brewery'
  ],
  lon: [
    -75.47489238, -73.41443291, -73.02160630, -73.34515821,
    -77.06089704,-75.43229951, -76.6221100, -76.15406625, 
    -75.75153202, -77.4416792, -78.8458326, -74.3600330,
    -72.45457030, -73.85581400, -77.38938696, -78.87345260,
    -76.82281329, -77.27866055, -78.86103739, -77.58669400
  ],
  lat: [
      44.33237311, 40.7550515,40.75913445, 42.92661444,
      42.15025771,43.20521338,42.0198710,43.04804637,43.07857637,
      43.0988098,42.8758185,41.3354040,41.0415525,40.8721114,
      42.89268134, 42.88479670, 42.67724221, 42.88851165, 42.86640421,
      43.1632750
  ],
  marker: {
      size: 7,
      color: [
          '#bebada', '#fdb462', '#fb8072', '#d9d9d9', '#bc80bd',
          '#b3de69', '#8dd3c7', '#80b1d3', '#fccde5', '#ffffb3'
      ],
      line: {
          width: 1
      }
  },
  name: 'New York Breweries',
  textposition: [
      'top right', 'top left', 'top center', 'bottom right', 'top right',
      'top left', 'bottom right', 'bottom left', 'top right', 'top right'
  ],
}];

var layout = {
  title: 'New York Breweries',
  font: {
      family: 'Droid Serif, serif',
      size: 6
  },
  titlefont: {
      size: 16
  },
  geo: {
      scope: 'New York',
      resolution: 50,
      lonaxis: {
          'range': [-161.75583,  -68.01197]
      },
      lataxis: {
          'range': [19.50139, 64.85694]
      },
      showrivers: true,
      rivercolor: '#fff',
      showlakes: true,
      lakecolor: '#fff',
      showland: true,
      landcolor: '#EAEAAE',
      countrycolor: '#d3d3d3',
      countrywidth: 1.5,
      subunitcolor: '#d3d3d3'
  }
};

Plotly.newPlot('myDiv', data, layout);
}