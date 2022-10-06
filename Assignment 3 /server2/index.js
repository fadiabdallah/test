const express= require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app= express();
const mysql = require('mysql2');
const sortJsonArray = require('sort-json-array');

const db = mysql.createPool({
  host:'localhost',
  user:'root',
  password:'Fadfouda23082001',
  database:'cruddatabase',
});

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));


app.post("/api/search", (req, res) => {

  const Name= req.body.movieName;
  console.log("hi",Name)
  const sqlSelect ="SELECT * FROM movie_reviews WHERE movieName= ? ";
  db.query(sqlSelect,Name, (err, result)=>{
    res.send(result);
    console.log(result);
  });
}); 

app.get("/api/get", (req, res) => {
  const sqlSelect ="SELECT * FROM movie_reviews ORDER BY movieName";
  db.query(sqlSelect, (err, result)=>{
    res.send(result);
    console.log(result);
  });
}); 

app.post('/api/insert', (req,res) => {

  const Name= req.body.movieName;
  const Review= req.body.movieReview;
  console.log("hey",Name , Review);
  const values = [[Name, Review]];
  const sqlInsert =
  "INSERT INTO movie_reviews (movieName, movieReview) VALUES ?";
  db.query(sqlInsert, [values], (err, res)=>{
    console.log(res);
  });
});

app.delete('/api/delete/:movieName', (req,result) => {
  const name = req.params.movieName;
  const sqlDelete ="DELETE FROM movie_reviews WHERE movieName = ?";

  db.query(sqlDelete, name, (err, result) => {
    if (err) console.log(err);
  });
});

app.put("/api/update", (req,res) => {
  const name = req.body.movieName;
  const review = req.body.movieReview;
  const sqlUpdate ="UPDATE movie_reviews SET movieReview = ? WHERE movieName = ?";

  db.query(sqlUpdate, [review, name], (err, result) => {
    if (err) console.log(err);
  });
});



app.listen(3001, ()=>{
  console.log("Server up and running on port 3001");
});
