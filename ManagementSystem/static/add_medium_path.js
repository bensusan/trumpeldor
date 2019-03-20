let short_path_points_for_medium = JSON.parse(localStorage.getItem("the_points_of_the_short_path"));
window.onload=function () {
    getRequestAttractions(markAttractionsOfMediumPath);
};

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
        if(true) {
            alert("if point in:"+short_path_points_for_medium.includes(pos) +"\nthe point attr: "+pos+"\n the arr: "+short_path_points_for_medium);

            // localStorage.setItem("title" + pos, "attraction ID: " + attr['id'] + "\nattraction name: " + attr['name'] + "\nposition: (" + attr['x'] + "," + attr['y'] + ")");
            // markAttractionOfMediumPath(pos);
        }
    });
}

function markAttractionOfMediumPath(pos){
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

