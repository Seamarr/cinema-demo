import React from 'react'
import './App.css'

class MoviesShow extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      movieList: [],
    };
  }

  componentWillMount(){
    this.fetchMovies()
  }

  fetchMovies = () => {
    console.log('Fetching..')

    fetch('http://localhost:8000/api/movie-list/')
    .then(response => response.json())
    .then(data => {
      this.setState({
        movieList:data,
      })
      console.log(data)
    })
  }


  render(){
    var movies = this.state.movieList
    return(
      <div>
          <center><h1>Seamar's Cinema</h1></center>
          <div className="ui grid container">
            {movies.map((movie) => {
              return(
                <div key={movie.id} className="four wide column">
                  <div>
                    <div className="titleImage"><h4 style={{cursor:"pointer"}} onClick={this.props.onClick}>{movie.title}</h4></div><img src={movie.movieImage} alt="Movie cover not loading"/>
                  </div>
                  <div>{movie.description}</div>
                </div>
              )
            })}
          </div>
      </div>
    )
  }
}

export default MoviesShow;
