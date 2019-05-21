//from django.conf import settings
let countOfPoints = 1;
let curPosClicked;
let curMarker;
let coordinates_of_last_click;
let arrOfPoints = [];
// let points= [
//     {lat: 31.263465932844372, lng: 34.801946282386783},
//     {lat: 31.263065932844372, lng: 34.801146282386783},
//     {lat: 31.263865932844372, lng: 34.802146282386783},
//     {lat: 31.262773527283052, lng: 34.802075028419495}
// ];
let map;
//
window.onload=function () {

    let ok1 = document.getElementById('ok1');
    let ok2 = document.getElementById('ok2');
    let ok3 = document.getElementById('ok3');
    let ok4 = document.getElementById('ok4');

    ok2.style.display = 'none';
    ok3.style.display = 'none';
    ok4.style.display = 'none';

    ok1.addEventListener('click',function () {
        ok2.style.display = '';
        ok1.style.display = 'none';


        let x = document.getElementById('lat'+countOfPoints);
        let y = document.getElementById('lng'+countOfPoints);
        let pointToMark = positionInMap(x.value, y.value);
        arrOfPoints.push(pointToMark);
        let theMark = markAttraction(pointToMark);
        countOfPoints++;
        markArr();
    });

    ok2.addEventListener('click',function () {
        ok3.style.display = '';
        ok2.style.display = 'none';
        countOfPoints++;
    });

    ok3.addEventListener('click',function () {
        ok4.style.display = '';
        ok3.style.display = 'none';
        countOfPoints++;
    });

    ok4.addEventListener('click',function () {
        ok4.style.display = 'none';
        countOfPoints++;
    });

};

function initMapAndAttractionsprop(){
    initMap();
    initAttractionsMarkers();
}

function initMap() {
     map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: {lat: 31.262860, lng: 34.801753}
    });
    // initAttractionsMarkers();
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


          prev_m=m;
           // markSpecificAttraction(pos);
          // alert("the point "+m.position);
  });
  }

function listenerForMap(map){
    google.maps.event.addListener(map, 'click', (function(event) {
        coordinates_of_last_click=event.latLng;

        if(countOfPoints<5) {
            let x = document.getElementById('lat' + countOfPoints);
            let y = document.getElementById('lng' + countOfPoints);
            x.value = coordinates_of_last_click.lat();
            y.value = coordinates_of_last_click.lng();
        }

        if(curPosClicked) {
            curMarker.setMap(null);
        }
        markArr();
        curPosClicked = positionInMap(event.latLng.lat(), event.latLng.lng());
        curMarker = markAttraction(curPosClicked);
    }));
}


function initAttractionsMarkers() {
    getRequestAttractions(markAttractions);
}

function getRequestAttractions(funcOnAttractions){
    // the server port and my ip
    serverRequest("GET", funcOnAttractions, 'http://'+ip+':12344/managementsystem/attraction/?format=json');
    //alert("need to remove this alert and fix funcToGetAttraction()!");
}

function markAttractions(attractionsJSON){
    //alert(window.innerHeight + " "+ window.innerWidth);
    attractionsJSON.forEach(function (attr) {

        let pos = {lat: attr['x'], lng: attr['y']};
        marker_arr.push(pos);
        localStorage.setItem("title"+pos,"attraction ID: "+attr['id']+"\nattraction name: "+attr['name']+"\nposition: ("+attr['x']+","+attr['y']+")");
        markAttraction(pos);
        // var currPoints = JSON.parse(localStorage.getItem("points"));
        // currPoints.push(x.position);
        // localStorage.setItem("points",JSON.stringify(currPoints));


    });
}


function markAttraction(pos){
        let marker = new google.maps.Marker({
          position: pos,
          map: map,
          icon: {
                url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
                }
        });
        // marker_arr.push(marker);
        marker.setMap(map);
        addEditListener(marker);
        return marker;
}

function positionInMap(lat, lng){
          return {lat: lat, lng: lng};
      }


function markArr() {
  for(let i=0;i<arrOfPoints.length;i++){
      let p = arrOfPoints[i];
      markAttraction(p);
  }
}