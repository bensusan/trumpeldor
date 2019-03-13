
const Http = new XMLHttpRequest();


function serverRequest(getOrPost, functionOnReady, url){
    Http.onreadystatechange = function(){
        if(Http.readyState == 4 && Http.status == 200){
            functionOnReady(JSON.parse(Http.responseText));
        }
    }
    Http.open(getOrPost, url);
    Http.send();
}

function markAttractions(attractionsJSON){
    attractionsJSON.forEach(function (attr) {
        let pos = {lat: attr['x'], lng: attr['y']};
        markAttraction(pos);
    });
}

function markAttraction(pos){
        let marker = new google.maps.Marker({
          position: pos,
          map: map
        });
        marker.setMap(map);
        return marker;
}


function getRequestAttractions(funcOnAttractions){
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // serverRequest("GET", funcOnAttractions, 'http://http://132.73.215.60:12345/managementsystem/attraction/?format=json');
    serverRequest("GET", funcOnAttractions, 'http://http://132.73.215.60:12344/managementsystem/attraction/?format=json');
}

function initAttractionsMarkers() {
    getRequestAttractions(markAttractions);
}

// function addAttraction(pos){
//           if(!currPointClicked)
//               currPointClicked = JSON.parse(localStorage.getItem('currPoint'));
//           let name = document.getElementById('name').value;
//           let descp = document.getElementById('description').value;
//           pointToAdd = {name:name, x:currPointClicked.lat, y:currPointClicked.lng, description:descp, picturesURLS:{}, videosURLS:{}};
//     Http.open("POST", attractionsURL, true);
// Http.setRequestHeader('Content-type','application/json; charset=utf-8');
// Http.onload = function () {
//     alert(pointToAdd.x +" ");
//
// }
// Http.send(JSON.stringify(pointToAdd));
//     window.location.href = "http://132.72.23.64:12345/managementsystem/main/map/";
//     return false;
// }