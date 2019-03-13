
const Http = new XMLHttpRequest();


function serverRequest(getOrPost, functionOnReady, url, post = null){
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
    serverRequest("GET", funcOnAttractions, 'http://132.72.23.64:12344/managementsystem/attraction/?format=json');
}

function initAttractionsMarkers() {
    getRequestAttractions(markAttractions);
}


function postRequestAttraction(attraction){
    serverRequest("POST", function noop(dummy){}, 'http://192.168.1.12:12344/managementsystem/attraction/',
        JSON.stringify(attraction));
}