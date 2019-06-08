function buildPlot() {
    /* data route */
  var url = "/api";
  d3.json(url).then(function(response) {

    console.log(response);

    var data = [response];

    var layout = {
      title: "Customer Ratings",
      xaxis: {
        title: "Rating"
      },
      yaxis: {
        title: "Count"
      }
    };

    Plotly.newPlot("plot", data, layout);
  });
}

buildPlot();

function tracebuildPlot() {
  /* data route */
var url = "/api2";
d3.json(url).then(function(response) {

  console.log(response);

  var data = [response];

  var layout = {
    title:"Review Locations",
    height: 400,
    width: 500
  };

  Plotly.newPlot("pie", data, layout);
});
}

tracebuildPlot();

function tracePlot() {
  /* data route */
var url = "/api3";
d3.json(url).then(function(response) {

  console.log(response);

  var data = [response];

  var layout = {
    title: "Bigram Frequencies",
   
  };

  Plotly.newPlot("line", data, layout);
});
}

tracePlot();

