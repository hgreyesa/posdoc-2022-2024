
// Select the database to use.
use('semarnat');

// Here we run an aggregation and open a cursor to the results.
// Use '.toArray()' to exhaust the cursor to return the whole result set.
// You can use '.hasNext()/.next()' to iterate through the cursor page by page.


result = db.getCollection('retc_2004_2022_complete').aggregate([
  // Find all of the sales that occurred in 2014.
  { $match: { "iarc_group": "1" } },
  //{ $match: { "cas": "7440-38-2" } },
  // Group the total sales for each product.
  { $group: { _id: [{"cas": "$cas"}, {"sustancia": "$sustancia"}] } },
  { $project: {
    "_id":0,
    "cas": "$_id.cas",
    "sustancia": "$_id.sustancia"
  }},
  { $sort: {
    "sustancia": 1
  }}

]);

/*
result.forEach(element => {

  msj = element["cas"] + " - " +  element["sustancia"]
  print(msj)
});*/


//db.getCollection("retc_2004_2022_complete").distinct("cas", {"iarc_group":"1"})
//db.getCollection("retc_2004_2022_complete").distinct("cas")



//db.getCollection('retc_2004_2022_complete').aggregate([
//  // Find all of the sales that occurred in 2014.
//  //{ $match: { "iarc_group": "1" } },
//  //{ $match: { "cas": "7440-38-2" } },
//  // Group the total sales for each product.
//  { $group: { _id: [{"cas": "$cas"}, {"sustancia": "$sustancia"}] } },
//  { $project: {
//    "_id":0,
//    "cas": "$_id.cas",
//    "sustancia": "$_id.sustancia"
//  }},
//  { $sort: {
//    "sustancia": 1
//  }}
//
//]);




