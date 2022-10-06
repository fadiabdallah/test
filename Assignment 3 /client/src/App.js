import React, {useState, useEffect} from "react";
import './App.css';
import Axios from 'axios';


function App() {
  const [movieName, setMovieName]= useState("");
  const [movieSearch, setMovieSearch]= useState("");
  const [reviewSearch, setReviewSearch]= useState("");
  const [review, setReview]= useState("");
  const [movieReviewList, setMovieList]=useState([]);

  const [newReview, setNewReview]= useState("");
  



  useEffect(()=>{
    Axios.get("http://localhost:3001/api/get").then((response) => {
      setMovieList(response.data); 
    });
  
  },   
  []);
  const mySearch=()=>{
    console.log("hi")
    Axios.post("http://localhost:3001/api/search", {
      movieName: movieSearch
    }).then((response) => {
      console.log(response.data);
      setReviewSearch(response.data[0].movieReview);
    }, (error) => {               
      console.log(error);
    });
 };

  const submitReview=()=>{
    console.log(movieName , review);
    Axios.post("http://localhost:3001/api/insert", {
      movieName: movieName,
      movieReview: review,
    });

      setMovieList([
        {movieName: movieName, movieReview: review }
      ]);
 };


 const deleteReview = (movie) => {
    console.log("hi",movie);
   Axios.delete(`http://localhost:3001/api/delete/${movie}`);
 };

 const updateReview = (movie) => {
   Axios.put("http://localhost:3001/api/update", {
     movieName: movie,
     movieReview: newReview,
   });
   setNewReview("")
 };

  return (
    <div className="App"><h1> CRUD APPLICATION </h1>
    <div className="form">
    <label>Movie Name:</label>
    <input type="text" name="movieName" onChange={(e)=>{
      setMovieName(e.target.value)
    }}/>
    <label>Review:</label>
    <input type="text" name="Review" onChange={(e)=>{
      setReview(e.target.value)
    }}/>


    <button onClick={submitReview}> Submit </button>
    <input type="text" name="Review" onChange={(e)=>{ 
        setMovieSearch(e.target.value)}}
    />
    <button onClick = {() => mySearch()}> Search </button>

    <label>{reviewSearch}</label> 
    



    {movieReviewList.map((val)=>{
      return (
        <div className="card">
          <h1> {val.movieName} </h1>
          <p> {val.movieReview} </p>

          <button onClick={() => {deleteReview(val.movieName)}}>Delete</button>
          <input type="text" id="updateInput" onChange={(e) => {setNewReview(e.target.value)}}/>
          <button onClick={()=> {updateReview(val.movieName)}}>Update</button>
        </div>
      );
    })}
  </div>
</div>
);
}

export default App;
