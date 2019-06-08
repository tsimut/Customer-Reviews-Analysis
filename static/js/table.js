
var tables= new Tabulator("#table", {
  ajaxURL:"/api4", //set initial table data
   
  columns:[
      {title:"Date", field:"Date Reviewed"},
      {title:"Name", field:"Name"},
      {title:"Rating", field:"Rating",headerFilter:"true"},
      {title:"Review", field:"Review",headerFilter:"true"}
  ],
});

table.setFilter([
  {field:"Date Reviewed"}, //filter by age greater than 52
  {field:"Rating"}, //and by height less than 142
  {field:"Review"}, 
]);