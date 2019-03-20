let short_path_points_for_medium = JSON.parse(localStorage.getItem("the_points_of_the_short_path"));
let short_path_points_for_medium_lat = [];
let short_path_points_for_medium_lng = [];


function initMapAndAttractionss(){
    short_path_points_for_medium = JSON.parse(localStorage.getItem("the_points_of_the_short_path"));
    short_path_points_for_medium_lat = [];
    short_path_points_for_medium_lng = [];
    let i;
    for(i=0;i<short_path_points_for_medium.length;i++)
    {
        short_path_points_for_medium_lat.push(short_path_points_for_medium[i].lat);
        short_path_points_for_medium_lng.push(short_path_points_for_medium[i].lng);
    }

    getRequestAttractions(markAttractionsOfMediumPath);
    initMapp();
    initAttractionsMarkersOfMediumPath();
}

function initMapp() {
     map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: {lat: 31.262860, lng: 34.801753}
    });

   initAttractionsMarkersOfMediumPath();
    listenerForMap();
   // initPoints();

}

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
        let lats=short_path_points_for_medium_lat.map(function (x){return x.toFixed(8)});
        let lngs=short_path_points_for_medium_lng.map(function (x){return x.toFixed(8)});
        let firstBool = lats.includes((pos.lat).toFixed(8));
        let secondBool = lngs.includes((pos.lng).toFixed(8));
        if(firstBool && secondBool) {
            // alert("if point in:"+lats.includes((pos.lat).toFixed(8)) +lngs.includes((pos.lng).toFixed(8)));
            localStorage.setItem("title" + pos, "attraction ID: " + attr['id'] + "\nattraction name: " + attr['name'] + "\nposition: (" + attr['x'] + "," + attr['y'] + ")");
            markAttractionOfMediumPath(pos);
        }
        else{
            localStorage.setItem("title" + pos, "attraction ID: " + attr['id'] + "\nattraction name: " + attr['name'] + "\nposition: (" + attr['x'] + "," + attr['y'] + ")");
            markAttraction(pos);
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

