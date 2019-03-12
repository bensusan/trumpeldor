//from django.conf import settings
let curPosClicked;
let curMarker;
let coordinates_of_last_click;
// let points= [
//     {lat: 31.263465932844372, lng: 34.801946282386783},
//     {lat: 31.263065932844372, lng: 34.801146282386783},
//     {lat: 31.263865932844372, lng: 34.802146282386783},
//     {lat: 31.262773527283052, lng: 34.802075028419495}
// ];

let points = JSON.parse(localStorage.getItem("points"));

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
    alert("the number of points is now :" + points.length)
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
      title: "Point no."+(num+1)
    });
    m.setMap(map);

    // localStorage.setItem("editedNum", num);
    //
    // localStorage.setItem("attr_name"+num, "the name of point no."+num);
    // localStorage.setItem("desc"+num, "the description of point no."+num);
    // localStorage.setItem("ques"+num, "the question of point no."+num);
    // localStorage.setItem("ans1"+num, "ans1 of point no."+num);
    // localStorage.setItem("ans2"+num, "ans2 of point no."+num);
    // localStorage.setItem("ans3"+num, "ans3 of point no."+num);
    // localStorage.setItem("ans4"+num, "ans4 of point no."+num);
    // localStorage.setItem("path_len"+num, "1");

    m.addListener('click', function() {
        alert("ppppp: "+num);


    var editBTN = document.getElementById('edit_attraction');
        editBTN.addEventListener('click', function(event) {
            localStorage.setItem("edited", m.position);
            localStorage.setItem("editedNum", num);
            window.location.href='/edit_attraction';
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

        var addBTN = document.getElementById('add_attraction');
        addBTN.addEventListener('click', function(event) {
        localStorage.setItem("addedPoint", JSON.stringify(coordinates_of_last_click));
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