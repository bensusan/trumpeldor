//from django.conf import settings

let curPosClicked;
let curMarker;
let coordinates_of_last_click;

let points = JSON.parse(localStorage.getItem("points"));
let pointsOfPath = [];

function initMapAndAttractions(){
    initMap();
    initAttractionsMarkers();
}

function initMap() {
     map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: {lat: 31.262860, lng: 34.801753}
    });
    initAttractionsMarkers();
    listenerForMap(map);
    initPoints();

}



  function initPoints(){
  for (var i = 0; i < points.length; i++) {
    addPoint2(points[i],i)
  }
  }

  function addPoint2(p,num){
    var myLatLng = {lat: p.lat, lng: p.lng};
    var m = new google.maps.Marker({
      position:myLatLng,
      map: map,
      title: "Point no."+(num+1)+".\n Belongs to the "+localStorage.getItem("path_len"+num) +" path."
    });
    m.setMap(map);

  }

  function addEditListener(m) {
      m.addListener('click', function() {
        var i=0;
        var addToPathBTN = document.getElementById('add_to_path');
        addToPathBTN.addEventListener('click', function() {
            if(i==0) {
                pointsOfPath.push(m.position);
                i++;
            }
            alert("point been added! now its: "+ pointsOfPath.toString());
        });
  });
  }

  function listenerForMap(map){
    google.maps.event.addListener(map, 'click', (function(event) {
        coordinates_of_last_click=event.latLng;

        if(curPosClicked) {
            curMarker.setMap(null);
        }

        curPosClicked = positionInMap(event.latLng.lat(), event.latLng.lng());
        curMarker = markAttraction(curPosClicked);
        var addBTN = document.getElementById('finish');
        addBTN.addEventListener('click', function(event) {
        // localStorage.setItem("addedPoint", JSON.stringify(curPosClicked));
            let pos = {lat: curPosClicked.lat, lng: curPosClicked.lng};
            // markAttraction(pos);
            localStorage.setItem("addedPoint", JSON.stringify(pos));
            // alert("this is what: "+ pos.lat +", " + pos.lng + ", "+ (typeof pos.lat));
            window.location.href='/edit_path';
        });
    }));
}
//
// function listenerForMap(map){
//     google.maps.event.addListener(map, 'click', (function() {
//
//         var finishBTN = document.getElementById('finish');
//         finishBTN.addEventListener('click', function() {
//             alert("very done!");
//             localStorage.setItem("the_points_of_the_path", JSON.stringify(pointsOfPath));
//
//             window.location.href='/edit_path';
//         });
//     }));
// }


function addListenerForMarker(marker) {
     google.maps.event.addListener(marker, 'click', (function(event) {
              return function() {
              }
          })(event));

}

function positionInMap(lat, lng){
          return {lat: lat, lng: lng};
      }