//from django.conf import settings
let curPosClicked;
let curMarker;
let coordinates_of_last_click;
let points= [
    {lat: 31.263465932844372, lng: 34.80194628238678},
    {lat: 31.3114324, lng: 34.5555555555555},
    {lat: 31.45255555372, lng: 34.9238678},
    {lat: 31.262773527283052, lng: 34.802075028419495}
];

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
    initPoints();
}

  function initPoints(){
  for (var i = 0; i < points.length; i++) {
    addPoint2(points[i])
  }
  }

  function addPoint2(p){
    var myLatLng = {lat: p.lat, lng: p.lng};
    var m = new google.maps.Marker({
      position:myLatLng,
      map: map,
      title: 'Hello World!'
    });
    m.setMap(map);
  }

function listenerForMap(map){
    google.maps.event.addListener(map, 'click', (function(event) {
        coordinates_of_last_click=event.latLng;
        if(curPosClicked) {
            curMarker.setMap(null);
        }
        curPosClicked = positionInMap(event.latLng.lat(), event.latLng.lng());
        curMarker = markAttraction(curPosClicked);
        editBTN=document.getElementById('edit_attraction');
        editBTN.addEventListener('click', function(event) {
        if(points.indexOf(curPosClicked)!=-1)
            {}
        });
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