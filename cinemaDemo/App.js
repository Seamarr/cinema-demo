import React from 'react'
import './App.css'
import MoviesShow from './moviesShow'
import SeatLoader from './SeatLoader'

class App extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      activeMovie:{
        id:null,
        seats:[],
        title:'',
      },
      selected:false,
    };
  }

  movieClick = e => {
    this.setState({
      selected: this.state.selected,
      activeMovie:{
        id:null,
        seats:[],
        title:e.target.innerHTML,
      }
    })

    let curMovieId = 'no id'

    fetch('http://localhost:8000/api/movie-list/')
    .then(response => response.json())
    .then(data => {
      data.map((movie) => {
        if(movie.title === this.state.activeMovie.title) {
          curMovieId = movie.id
        }
      })
      this.setState({
        selected: !this.state.selected,
        activeMovie:{
          id:curMovieId,
          seats:[],
          title:this.state.activeMovie.title,
        }
      })
      console.log(this.state.activeMovie.id)
    })
  }

  goBack = () => {
    this.setState({
      selected:!this.state.selected,
    })
  }



  render() {
    var self = this
    return (
      <div>
        {!this.state.selected ? <MoviesShow onClick={this.movieClick}/> : <SeatLoader goBack={this.movieClick} movieId={this.state.activeMovie.id} movieName={this.state.activeMovie.title} />}
      </div>
    );
  }
}

export default App;
