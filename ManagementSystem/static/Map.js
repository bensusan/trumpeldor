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

window.onload=function () {
    let add_manually_menu = document.getElementById('add_manually_menu');
    add_manually_menu.addEventListener('click', function() {
            var the_manual_lat = document.getElementById("manual_lat");
            the_manual_lat.style.display = "inline";

            var the_manual_lng = document.getElementById("manual_lng");
            the_manual_lng.style.display = "inline";

            var add_manually_button = document.getElementById("add_manually");
            add_manually_button.style.display = "inline";
        });

    let addManuallyBTN = document.getElementById('add_manually');
        addManuallyBTN.addEventListener('click', function() {
            let manualLat = document.getElementById('manual_lat').value;
            let manualLng = document.getElementById('manual_lng').value;
            let pos = {lat: manualLat, lng: manualLng};
            // markAttraction(pos);
            localStorage.setItem("addedPoint", JSON.stringify(pos));
            // alert("this is what: "+ pos.lat +", " + pos.lng + ", "+ (typeof pos.lat));
            window.location.href='/add_attraction';
        });
};

function initMapAndAttractions(){
        //alert("dasmaps");
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
    // alert("the number of points is now :" + points.length)
    // var shortPath1 = JSON.parse(localStorage.getItem("short_path"));
    //     var medPath1 = JSON.parse(localStorage.getItem("medium_path"));
    //     var longPath1 = JSON.parse(localStorage.getItem("long_path"));
          // alert("short:"+shortPath1.length +"\nmedium: "+medPath1.length +"\nlong: "+longPath1.length);


}


  function addEditListener(m) {
      m.addListener('click', function() {

          if(prev_m!=1) {

              prev_m.setIcon(prev_icon);
          }
          //alert("sda");
          prev_icon=m.icon;
          m.setIcon("http://maps.google.com/mapfiles/ms/icons/pink-dot.png");

          prev_m=m;
           // markSpecificAttraction(pos);
          // alert("the point "+m.position);
        var editBTN = document.getElementById('edit_attraction');
        editBTN.addEventListener('click', function() {
            localStorage.setItem("edited", JSON.stringify(m.position));
            window.location.href='/edit_attraction';
        });
  });
  }

function listenerForMap(map){
    google.maps.event.addListener(map, 'click', (function(event) {
        coordinates_of_last_click=event.latLng;
        // alert(coordinates_of_last_click.lat()+","+coordinates_of_last_click.lng())
        // alert(coordinates_of_last_click);
        if(curPosClicked) {
            curMarker.setMap(null);
        }

        curPosClicked = positionInMap(event.latLng.lat(), event.latLng.lng());
        curMarker = markAttraction(curPosClicked);
        var addBTN = document.getElementById('add_attraction');
        addBTN.addEventListener('click', function(event) {
        // localStorage.setItem("addedPoint", JSON.stringify(curPosClicked));
            let pos = {lat: curPosClicked.lat, lng: curPosClicked.lng};
            // markAttraction(pos);
            localStorage.setItem("addedPoint", JSON.stringify(pos));
            // alert("this is what: "+ pos.lat +", " + pos.lng + ", "+ (typeof pos.lat));
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

