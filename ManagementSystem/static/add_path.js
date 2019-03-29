//from django.conf import settings

// alert("aaaaaaaa");

// let curPosClicked;
// let curMarker;
// let coordinates_of_last_click;
var str_of_points="";
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
    listenerForMap();
   // initPoints();

}



  function initPoints(){
  for (var i = 0; i < points.length; i++) {
    addPoint2(points[i],i);
      localStorage.setItem("i" + i, "0");
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

        var addToPathBTN = document.getElementById('add_reg_to_path');
        addToPathBTN.addEventListener('click', function() {
            if(pointsOfPath.indexOf(m.position)==-1)
            {
                // alert("only once!");
                pointsOfPath.push(m.position);
                str_of_points=str_of_points+m.position+"<br />";
            }
            // alert(str_of_points);
            document.getElementById("showing_added_points").innerHTML = str_of_points ;
           // alert("point been added! now its: "+ pointsOfPath.toString());
        });
  });
  }


function listenerForMap(){
        var finishBTN = document.getElementById('finish_reg');
        finishBTN.addEventListener('click', function() {
            localStorage.setItem("the_points_of_the_path", JSON.stringify(pointsOfPath));
            
            window.location.href='/edit_path';
        });
}

// function postRequestTrack() {
//
// }

// function addListenerForMarker(marker) {
//      google.maps.event.addListener(marker, 'click', (function(event) {
//               return function() {
//               }
//           })(event));
//
// }
//
// function positionInMap(lat, lng){
//           return {lat: lat, lng: lng};
//       }