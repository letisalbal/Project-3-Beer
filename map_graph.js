Plotly.d3.csv('brewerylocations.csv', function(err, rows){

  var classArray = unpack(rows, 'class');
  var classes = [...new Set(classArray)];

  function unpack(rows, key) {
    return rows.map(function(row) { return row[key]; });
  }

  var data = classes.map(function(classes) {
    var rowsFiltered = rows.filter(function(row) {
        return (row.class === classes);
    });
    return {
       type: 'scattermapbox',
       name: classes,
       lat: unpack(rowsFiltered, 'reclat'),
       lon: unpack(rowsFiltered, 'reclong')
    };
  });

  var layout = {
	 title: 'New York Breweries',
	 font: {
		 color: 'white'
	 },
    dragmode: 'zoom',
    mapbox: {
      center: {
        lat: 40.730610,
        lon: -73.935242
      },
      domain: {
        x: [0, 1],
        y: [0, 1]
      },
      style: 'dark',
      zoom: 1
    },
    margin: {
      r: 20,
      t: 40,
      b: 20,
      l: 20,
      pad: 0
    },
    paper_bgcolor: '#191A1A',
    plot_bgcolor: '#191A1A',
    showlegend: true,
	 annotations: [{
		 x: 0,
       y: 0,
       xref: 'paper',
       yref: 'paper',
		 showarrow: false
	 }]
  };

  Plotly.setPlotConfig({
    mapboxAccessToken: 'pk.eyJ1IjoiYXNtaXRoNTQ0NiIsImEiOiJjazN0MmlhbGUwZGlzM2ZvOTI5b2p6eHVnIn0.JhIaLCCiyv9cbSpW4IOl9w'
  });

  Plotly.plot('myDiv', data, layout);
});