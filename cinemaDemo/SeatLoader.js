import React from 'react'
import './App.css'
import normalSeat from './seat.png'
import greenSeat from './greenSeat.png'
import greySeat from './greySeat.png'

class SeatLoader extends React.Component {
  constructor(props){
    super(props);

    this.state = {
      seatList: [],
      currentSeat:{
        id:null,
        label:'',
        selected: false,
      },
      selectedSeats:[],
    }
  }


  getCookie = name => {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

  componentWillMount(){
    this.fetchSeats()
  }

  fetchSeats = (props) => {
    fetch('http://localhost:8000/api/seat-list/')
    .then(response => response.json())
    .then(data => {
      data.map((seat) => {
        if(this.props.movieId === seat.corMovie){
          this.setState({
            seatList: [...this.state.seatList, seat]
          })
        }
      })
    })
  }

  makeSelect(seat) {
    seat.isSelected = !seat.isSelected
    var csrftoken = this.getCookie('csrftoken')
    var url = `http://localhost:8000/api/seat-update/${seat.id}/`

    fetch(url, {
      method:'POST',
      headers:{
        'Content-type':'application/json',
        'X-CSRFToken': csrftoken,
      },
      body:JSON.stringify({'isSelected': seat.isSelected, 'isReserved': seat.isReserved, 'corMovie': seat.corMovie, 'label':seat.label})
    }).then(() => {
      this.setState({
        seatList:[],
      })
      this.fetchSeats()
    })

    console.log('SEAT:', seat.isSelected)
  }

  render(){
    var self = this
    return(
      <div>
        <center><h1>{self.props.movieName}</h1></center>
        <div className="ui grid container">
          {self.state.seatList.map((seat, index) => {
            return(
              <div key={seat.id}>{seat.isReserved ? <img className="seatImg" src={greySeat}/> : seat.isSelected ? <img className="seatImg" onClick={() => this.makeSelect(seat)} style={{cursor:'pointer'}} src={greenSeat}/> : <img className="seatImg" onClick={() => this.makeSelect(seat)} style={{cursor:'pointer'}} src={normalSeat}/>}<div className="seatLabels">    {seat.label}</div></div>
            )
          })}
        </div>
        <div><button className="ui button" style={{float:'right', marginRight:'500px'}} onClick={self.props.goBack}>Back</button></div>
      </div>
    );
  }
}

export default SeatLoader;
