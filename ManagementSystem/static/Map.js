//from django.conf import settings
let curPosClicked;
let curMarker;
let coordinates_of_last_click;
let points= [
    {lat: 31.263465932844372, lng: 34.801946282386783},
    {lat: 31.263065932844372, lng: 34.801146282386783},
    {lat: 31.263865932844372, lng: 34.802146282386783},
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

    localStorage.setItem("editedNum", num);

    localStorage.setItem("ques"+num, "the question of p"+num);
    localStorage.setItem("ans1"+num, "the ans1 of p"+num);
    localStorage.setItem("ans2"+num, "the ans2 of p"+num);
    localStorage.setItem("ans3"+num, "the ans3 of p"+num);
    localStorage.setItem("ans4"+num, "the ans4 of p"+num);

    m.addListener('click', function() {
        alert("ppppp: "+num);

    var editBTN = document.getElementById('edit_attraction');
        editBTN.addEventListener('click', function(event) {
            localStorage.setItem("edited", m.position);
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

        // editBTN=document.getElementById('edit_attraction');
        // editBTN.addEventListener('click', function(event) {
        //     var ccc= points.indexOf(coordinates_of_last_click);
        //     //alert(coordinates_of_last_click +" and : : : "+ points);
        // if(ccc!=-1)
        //     {
        //         window.location.href='/edit_attraction';
        //     }
        // });

        var addBTN = document.getElementById('add_attraction');
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