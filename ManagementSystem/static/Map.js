//from django.conf import settings
let curPosClicked;
let curMarker;
let coordinates_of_last_click;

function initMapAndAttractions(){
    initMap();
    initAttractionsMarkers();
}
function initMap() {
     map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: {lat: 31.262860, lng: 34.801753}
    });
    listenerForMap(map);
}

function listenerForMap(map){
    google.maps.event.addListener(map, 'click', (function(event) {
        coordinates_of_last_click=event.latLng;
        if(curPosClicked) {
            curMarker.setMap(null);
        }
        curPosClicked = positionInMap(event.latLng.lat(), event.latLng.lng());
        curMarker = markAttraction(curPosClicked);
        addBTN = document.getElementById('add_attraction');
        addBTN.addEventListener('click', function(event) {
        localStorage.setItem("addedPoint", coordinates_of_last_click);
            window.location.href='/add_attraction';
        });
    }));
}


function addListenerForMarker(marker) {
     google.maps.event.addListener(marker, 'click', (function(event) {
              return function() {
              }
          })(event));

}

function positionInMap(lat, lng){
          return {lat: lat, lng: lng};
      }