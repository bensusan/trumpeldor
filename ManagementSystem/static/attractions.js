
const Http = new XMLHttpRequest();


function serverRequest(getOrPost, functionOnReady, url){
    Http.onreadystatechange = function(){
        if(Http.readyState == 4 && Http.status == 200){
            functionOnReady(JSON.parse(Http.responseText));
        }
    }
    Http.open(getOrPost, url, true);
    Http.send(null);
}

function getAttractions(attractionsJSON){
    attractionsJSON.forEach(function (attr) {
        let pos = {lat: attr['x'], lng: attr['y']};
        markAttraction(pos);
    });
}

function markAttraction(attr){

}

function getRequestAttractions(){
    serverRequest("GET", 'http://192.168.1.9:12345/attractions/');
}