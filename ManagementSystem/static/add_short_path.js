//from django.conf import settings

// alert("aaaaaaaa");

let curPosClicked;
// let curMarker;
// let coordinates_of_last_click;
var str_of_points="";
let points = JSON.parse(localStorage.getItem("points"));
let pointsOfPath = [];


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
  //
  //
  //
  // function initPoints(){
  // for (var i = 0; i < points.length; i++) {
  //   addPoint2(points[i],i);
  //     localStorage.setItem("i" + i, "0");
  // }
  // }
  //
  // function addPoint2(p,num){
  //   var myLatLng = {lat: p.lat, lng: p.lng};
  //   var m = new google.maps.Marker({
  //     position:myLatLng,
  //     map: map,
  //     title: "Point no."+(num+1)+".\n Belongs to the "+localStorage.getItem("path_len"+num) +" path."
  //   });
  //   m.setMap(map);
  //
  // }

  function addEditListener(m) {
      m.addListener('click', function() {
        curPosClicked=m.position;
        var addToPathBTN = document.getElementById('add_reg_to_path');
        addToPathBTN.addEventListener('click', function() {

            if(pointsOfPath.indexOf(m.position)==-1 && curPosClicked==m.position)
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
            localStorage.setItem("the_points_of_the_short_path", JSON.stringify(pointsOfPath));
            localStorage.setItem("the_points_of_the_finish_path", JSON.stringify(pointsOfPath));
            let short_to_send = {points:pointsOfPath,length:1};
            // let medium_to_send = {length:2,points:pointsOfPath};
            // let long_to_send = {length:3,points:pointsOfPath};
             postRequestShortPath(short_to_send);
             alert("alerto");
            // postRequestMediumPath(medium_to_send);
            // postRequestLongPath(long_to_send);

//the_points_of_the_short_path

            window.location.href='/edit_path';
        });

         var showwBTN = document.getElementById('showingshit');
        showwBTN.addEventListener('click', function() {
            getRequestPaths(doShitToDelete);
             alert("shit!");

        });
}


function doShitToDelete(pathsJSON) {

    pathsJSON.forEach(function (path) {
      alert("this: "+path.points);
    });

}

function getRequestPaths(funcOnPaths){
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    serverRequest("GET", funcOnPaths, 'http://10.0.0.4:12344/managementsystem/track/?format=json');
}

function getRequestShortPath(funcOnShortPath){
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    serverRequest("GET", funcOnShortPath, 'http://10.0.0.4:12344/managementsystem/track/1/?format=json');
}

function postRequestShortPath(short_path){
    alert("blatos");
    serverRequest("POST", function noop(dummy){}, 'http://10.0.0.4:12344/managementsystem/track/',
        JSON.stringify(short_path));
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
          // ,icon: {
          //       url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
          //       // https://medium.com/@letian1997/how-to-change-javascript-google-map-marker-color-8a72131d1207
          //       }
        });
        marker.setMap(map);
        addEditListener(marker);
        return marker;
}

function initAttractionsMarkersOfShortPath() {
    getRequestAttractions(markAttractionsOfShortPath);
}

