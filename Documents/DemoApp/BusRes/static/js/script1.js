const container = document.querySelector('.container');
const seats = document.querySelectorAll('.row .seat:not(.occupied)');
const count = document.getElementById('count');
const total = document.getElementById('total');

const no = document.getElementById('no');

const busid = document.getElementById('busid');
let idbus = +busid.value;

localStorage.setItem('BusId',idbus);

populateUI();



function updateSelectedCount(){
  const selectedSeats = document.querySelectorAll('.row .seat.selected');
  console.log("hello");
  console.log(selectedSeats);

  const seatsIndex = [...selectedSeats].map(function(seat){
    return [...seats].indexOf(seat);
  });
  console.log(seatsIndex)

  localStorage.setItem('selectedSeats',JSON.stringify(seatsIndex));


  const selectedSeatsCount=selectedSeats.length;


  const rate = document.getElementById('rate');

  no.value=seatsIndex;
  console.log(typeof(parseInt(seatsIndex)));
  count.value = selectedSeatsCount;
  total.value = (selectedSeatsCount*parseInt(rate.value))-parseInt(rate.value);

}


function populateUI(){
  const selectSeats =JSON.parse(localStorage.getItem('selectedSeats'));

  //no.innerText=selectSeats;

  if(selectSeats !== null && selectSeats.length >0){
    seats.forEach((seat,index)=>{
        if (selectSeats.indexOf(index)>-1){
          seat.classList.add('occupied');
        }
    })
  }

  const selectedBusIndex = localStorage.getItem('BusId');

  if (selectedBusIndex !== null) {
    movieSelect = selectedBusIndex;
  }

}



container.addEventListener('click',(e)=>{
  if(e.target.classList.contains('seat') && !e.target.classList.contains('occupied')){
    e.target.classList.toggle('selected');

  }

  updateSelectedCount();
  console.log("callSucc");


});


updateSelectedCount();
