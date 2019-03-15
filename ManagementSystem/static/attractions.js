
const Http = new XMLHttpRequest();


function serverRequest(getOrPost, functionOnReady, url, post=null){
    Http.onreadystatechange = function(){
        if(Http.readyState == 4 && Http.status == 200){
            functionOnReady(JSON.parse(Http.responseText));
        }
    }
    Http.open(getOrPost, url, true);
    if(post) {
        Http.setRequestHeader('Content-type','application/json; charset=utf-8');
        Http.send(post);
        window.location.href = '/attractions';
        return false;
    }
    Http.send();
}

function markAttractions(attractionsJSON){
    attractionsJSON.forEach(function (attr) {
        let pos = {lat: attr['x'], lng: attr['y']};
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
          title: "Point ("+pos.lat+","+pos.lng+")."
        });
        marker.setMap(map);
        addEditListener(marker);
        return marker;
}


function getRequestAttractions(funcOnAttractions){
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    serverRequest("GET", funcOnAttractions, 'http://10.0.0.7:12344/managementsystem/attraction/?format=json');
}

function initAttractionsMarkers() {
    getRequestAttractions(markAttractions);
}


function postRequestAttraction(attraction){
    alert("blat");
    serverRequest("POST", function noop(dummy){}, 'http://10.0.0.7:12344/managementsystem/attraction/',
        JSON.stringify(attraction));
}
