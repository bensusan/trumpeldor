//from django.conf import settings
let curPosClicked;
let curMarker;
let addAttractionBTN;
const mapHtml = document.getElementById('map');
const addAttractionTextToBTN = document.createTextNode("Add Attraction");


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
        if(curPosClicked) {
            curMarker.setMap(null);
        }
        curPosClicked = positionInMap(event.latLng.lat(), event.latLng.lng());
        curMarker = markAttraction(curPosClicked);
        addAttractionBTN = document.createElement("BUTTON");
        addAttractionBTN.appendChild(addAttractionTextToBTN);
        mapHtml.parentNode.insertBefore(addAttractionBTN, mapHtml);
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