var x;
var map;
var points= [
    // {lat: 31.263465932844372, lng: 34.80194628238678},
    // {lat: 31.262773527283052, lng: 34.802075028419495}
];
const Http = new XMLHttpRequest();
const attractionsURL ='http://132.72.23.64:12345/managementsystem/attractions/';
const tracksURL ='http://132.72.23.64:12345/managementsystem/tracks/';
let pointsForTrack=[];
let currPointClicked;
let marker;
const radius = 0.01;
let attrForTrack=[];


      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 18,
          center: {lat: 31.262860, lng: 34.801753}
        });
        initPoints(getAllPoints);
        addListener();
      }

      function addListener(){
          google.maps.event.addListener(map, 'click', (function(event) {
                  if (location.href == 'http://132.72.23.64:12345/managementsystem/main/map/' && currPointClicked) {
                      marker.setMap(null);
                      pointsForTrack = null;
                  }
                  currPointClicked = createPoint(event.latLng.lat(), event.latLng.lng());
                  markerPoint(currPointClicked);
          }));
      }

      function createPoint(lat, lng){
          return {lat: lat, lng: lng};
      }

      function initPoints(functionOnReady){
          Http.open("GET", attractionsURL);
          Http.send();
          Http.onreadystatechange = functionOnReady;
      }

      function markerPoint(p){
        let pointToMarker = {lat: p.lat, lng: p.lng};
        marker = new google.maps.Marker({
          position: pointToMarker,
          map: map
        });
        marker.setMap(map);
        //  marker.addListener(marker, 'click', function(event) {
        //      alert("fdfdf");
        //   currPointClicked = createPoint(event.latLng.lat(),event.latLng.lng());
        // })
          google.maps.event.addListener(marker, 'click', (function(event) {
              return function() {
                  //    currPointClicked = createPoint(event.latLng.lat(), event.latLng.lng());
                 if(location.href == 'http://132.72.23.64:12345/managementsystem/main/maptrack/'){
                  let bool = checkIfPointInRadius(marker);
                      if(bool > -1) {
                          attrForTrack.push(pointsForTrack[bool]);
                      }
              }
              }
          })(event));

      }


function getAllPoints(e){
          if (Http.readyState == 4 && Http.status == 200) {
                  let response = JSON.parse(Http.responseText);
                  for(let i = 0; i < response.length; i++){
                      points.push({lat : response[i].x, lng : response[i].y});
                      pointsForTrack.push(response[i]);
                  }
                  for(let i = 0; i < points.length; i++){
                      markerPoint(points[i]);
                  }
              }
}

function addPoint(){
          if(!currPointClicked)
              currPointClicked = JSON.parse(localStorage.getItem('currPoint'));
          let name = document.getElementById('name').value;
          let descp = document.getElementById('description').value;
          pointToAdd = {name:name, x:currPointClicked.lat, y:currPointClicked.lng, description:descp, picturesURLS:{}, videosURLS:{}};
    Http.open("POST", attractionsURL, true);
Http.setRequestHeader('Content-type','application/json; charset=utf-8');
Http.onload = function () {
    alert(pointToAdd.x +" ");

}
Http.send(JSON.stringify(pointToAdd));
    window.location.href = "http://132.72.23.64:12345/managementsystem/main/map/";
    return false;
}

function deletePoint(){
          alert("bg");
          alert(currPointClicked.lat+" bllllaaaa");
    var range = radius;
    let lat = currPointClicked.lat;
    let lng = currPointClicked.lng;
    var minLat = lat - range;
    var maxLat = lat + range;
    var minLng = lng - range;
    var maxLng = lng + range;

    for(let i = 0; i < points.length; i++){
        if(points[i].lat > minLat && points[i].lat < maxLat && points[i].lng > minLng && points[i].lng < maxLng){
            var url = "http://132.72.23.64:12345/managementsystem/main/attraction/" +  points[i].lat +"/" + points[i].lng;
            Http.open("DELETE", url+'/12', true);
            Http.onload = function () {
                alert("delete bitch");
            }
            Http.send(null);

        }
    }
}


function checkIfPointInRadius(p){
    var range = radius;
    let lat = p.lat;
    let lng = p.lng;
    for(let i = 0; i < pointsForTrack.length; i++){
        if(Math.abs(pointsForTrack[i].x - p.getPosition().lat()) < radius && Math.abs(pointsForTrack[i].y - p.getPosition().lng()) < radius)
            return i;
    }
    return -1;
}


function getIfPointExist(e){
          if (Http.readyState == 4 && Http.status == 200) {
                  currPointClicked = JSON.parse(Http.responseText);
              }
}
function addMoreAttributesToPoint(){
          if(currPointClicked) {
              localStorage.setItem('currPoint', JSON.stringify(currPointClicked));
              location.href = location.href + 'addattraction/'
          }
}


