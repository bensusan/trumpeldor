
function getRequestMediumPath(funcOnMedPath){
    // the server port and my ip
    serverRequest("GET", funcOnMedPath, 'http://10.0.0.7:12344/managementsystem/track/2/?format=json');
}

function postRequestMediumPath(medium_path){
    alert("med_blatos");
    serverRequest("POST", function noop(dummy){}, 'http://10.0.0.7:12344/managementsystem/track/2/',
        JSON.stringify(medium_path));
}


function markAttractionsOfMediumPath(attractionsJSON){
    attractionsJSON.forEach(function (attr) {
        let pos = {lat: attr['x'], lng: attr['y']};
        localStorage.setItem("title"+pos,"attraction ID: "+attr['id']+"\nattraction name: "+attr['name']+"\nposition: ("+attr['x']+","+attr['y']+")");
        markAttractionsOfMediumPath(pos);
        // var currPoints = JSON.parse(localStorage.getItem("points"));
        // currPoints.push(x.position);
        // localStorage.setItem("points",JSON.stringify(currPoints));


    });
}

function markAttractionsOfMediumPath(pos){
    let the_title=localStorage.getItem("title"+pos);
        let marker = new google.maps.Marker({
          position: pos,
          map: map,
          title:the_title
          ,icon: {
                url: "http://maps.google.com/mapfiles/ms/icons/orange-dot.png"
                // https://medium.com/@letian1997/how-to-change-javascript-google-map-marker-color-8a72131d1207
                }
        });
        marker.setMap(map);
        addEditListener(marker);
        return marker;
}

function initAttractionsMarkersOfMediumPath() {
    getRequestAttractions(markAttractionsOfMediumPath);
}

