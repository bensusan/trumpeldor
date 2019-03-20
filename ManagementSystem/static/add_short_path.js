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
    document.getElementById("things_to_fix").innerHTML = "need to fix: if we click on to points and then on the 'add' button it adds both of them." ;

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

function getRequestShortPath(funcOnShortPath){
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    serverRequest("GET", funcOnShortPath, 'http://10.0.0.7:12344/managementsystem/track/1/?format=json');
}

function postRequestShortPath(short_path){
    alert("blatos");
    serverRequest("POST", function noop(dummy){}, 'http://10.0.0.7:12344/managementsystem/track/1/',
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
          ,icon: {
                url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
                }
        });
        marker.setMap(map);
        addEditListener(marker);
        return marker;
}

function initAttractionsMarkersOfShortPath() {
    getRequestAttractions(markAttractionsOfShortPath);
}

