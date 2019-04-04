//from django.conf import settings
let curPosClicked;
// let curMarker;
// let coordinates_of_last_click;
var str_of_points="";
let points = JSON.parse(localStorage.getItem("points"));
let pointsOfPath = [];
let arr_of_complete_points = [];

function initMapAndAttractions(){
    initMap();
    initAttractionsMarkersOfShortPath();
}

function initMap() {
     map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: {lat: 31.262860, lng: 34.801753}
    });
    //initAttractionsMarkersOfShortPath();
    listenerForMap();
   // initPoints();

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
        curPosClicked=m.position;
        var addToPathBTN = document.getElementById('add_reg_to_path');
        addToPathBTN.addEventListener('click', function() {

            if(pointsOfPath.indexOf(m.position)==-1 && curPosClicked==m.position)
            {
                // alert("only once!");
                let point_to_push = {lat: m.position.lat().toFixed(8), lng: m.position.lng().toFixed(8)};
                pointsOfPath.push(point_to_push);
                str_of_points=str_of_points+m.position+"<br />";
            }
            // alert(str_of_points);
            var border = document.getElementById("border_of_points");
            border.style.display = "block";
            document.getElementById("showing_added_points").innerHTML = str_of_points;
            document.getElementById("showing_added_points").style.fontWeight = 'bold';

           // alert("point been added! now its: "+ pointsOfPath.toString());
        });
  });
  }


function listenerForMap(){
        var finishBTN = document.getElementById('finish_reg');
        finishBTN.addEventListener('click', function() {
            localStorage.setItem("the_points_of_the_short_path", JSON.stringify(pointsOfPath));
            localStorage.setItem("the_points_of_the_finish_path", JSON.stringify(pointsOfPath));
            getRequestAttractions(funcInOrderToGetAttractions);

        });

}

function funcInOrderToGetAttractions(attractionsJSON) {
      attractionsJSON.forEach(function (attr) {
        let pos = {lat: (attr['x']).toFixed(8), lng: (attr['y']).toFixed(8)};
        let lats=pointsOfPath.map(function (x){return x.lat});
        let lngs=pointsOfPath.map(function (x){return x.lng});
        let firstBool = lats.includes(pos.lat);
        let secondBool = lngs.includes(pos.lng);

  if(firstBool && secondBool) {
      let the_point = {id:attr['id'],name:attr['name'],x:attr['x'],y:attr['y'],description:attr['description'],picturesURLS:attr['picturesURLS'],videosURLS:attr['videosURLS']};
            arr_of_complete_points.push(the_point);
        }

      });
    //alert(arr_of_complete_points.length);
    let short_to_send = {points:arr_of_complete_points,length:1};
            // let medium_to_send = {points:arr_of_complete_points,length:2};
            // let long_to_send = {points:arr_of_complete_points,length:3};
            postRequestShortPath(short_to_send);
// Promise.all([postRequestShortPath(short_to_send),  postRequestShortPath(medium_to_send)]).then(function() {
//   postRequestShortPath(long_to_send);
// });
    //                         executeAsynchronously(
    // [ postRequestShortPath(short_to_send),  postRequestShortPath(medium_to_send),postRequestShortPath(long_to_send)], 10);
            //  postRequestShortPath(short_to_send);
            // postRequestShortPath(medium_to_send);
            // postRequestShortPath(long_to_send);

            window.location.href='/main';
}

function executeAsynchronously(functions, timeout) {
  for(let i = 0; i < functions.length; i++) {
    setTimeout(functions[i], timeout);
  }
}


function getRequestPaths(funcOnPaths){
    // the server port and my ip
    serverRequest("GET", funcOnPaths, 'http://'+ip+':12344/managementsystem/track/?format=json');
}

function getRequestShortPath(funcOnShortPath){
    // the server port and my ip
    serverRequest("GET", funcOnShortPath, 'http://'+ip+':12344/managementsystem/track/1/?format=json');
}

function postRequestShortPath(short_path){
   // alert("blatos");
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/track/',
        JSON.stringify(short_path));
        readyToMedium=1;
}


function markAttractionsOfShortPath(attractionsJSON){
    attractionsJSON.forEach(function (attr) {
        let pos = {lat: attr['x'], lng: attr['y']};
        localStorage.setItem("title"+pos,"attraction ID: "+attr['id']+"\nattraction name: "+attr['name']+"\nposition: ("+attr['x']+","+attr['y']+")");
        markAttractionOfShortPath(pos);
        // var currPoints = JSON.parse(localStorage.getItem("points"));
        // currPoints.push(x.position);
        // localStorage.setItem("points",JSON.stringify(currPoints));


    });
}

function markAttractionOfShortPath(pos){
    let the_title=localStorage.getItem("title"+pos);
        let marker = new google.maps.Marker({
          position: pos,
          map: map,
          title:the_title
          ,icon: {
                url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
                // https://medium.com/@letian1997/how-to-change-javascript-google-map-marker-color-8a72131d1207
                }
        });
        marker.setMap(map);
        addEditListener(marker);
        return marker;
}

function initAttractionsMarkersOfShortPath() {
    getRequestAttractions(markAttractionsOfShortPath);
}
