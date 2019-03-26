
let curPosClicked;

var str_of_points="";
let pointsOfPath = [];
let pointsOfShort = [];
let idOfMedium = 0;
let idOfLong = 0;

function initMapAndAttractionss(){
    str_of_points="";
    pointsOfPath = [];

    getRequestTracks(markAttractionsOfMediumPaths);
    initMapp();
    initAttractionsMarkersOfMediumPath();
}

  function addEditListenerr(m) {
      m.addListener('click', function() {
          curPosClicked=m.position;
        var addToPathBTN = document.getElementById('add_reg_to_path_med');
        addToPathBTN.addEventListener('click', function() {
            if(pointsOfPath.indexOf(m.position)==-1 && curPosClicked==m.position)
            {
                let point_to_push = {lat: m.position.lat(), lng: m.position.lng()};
                //let point_to_push2 = {lat: m.position.lat().toFixed(8), lng: m.position.lng().toFixed(8)};
                pointsOfPath.push(point_to_push);
                // pointsOfPath.push(m.position);
                str_of_points=str_of_points+m.position+"<br />";
            }
            // alert(str_of_points);
            document.getElementById("showing_added_points_med").innerHTML = str_of_points ;
           // alert("point been added! now its: "+ pointsOfPath.toString());
        });
  });
  }

function initMapp() {
     map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: {lat: 31.262860, lng: 34.801753}
    });
   //initAttractionsMarkersOfMediumPath();

    listenerForMappo();
   // initPoints();

}


function markAttractionsOfMediumPaths(tracksJSON){

    tracksJSON.forEach(function (track) {

        if(track['length']==2) {
            idOfMedium = track['id'];

            let points_of_track = track['points'];
            points_of_track.forEach(function (attr) {

                let pos2 = {lat: (attr['x']).toFixed(8), lng: (attr['y']).toFixed(8)};

                    let pos = {lat: attr['x'], lng: attr['y']};
                    pointsOfShort.push(pos2);
                    localStorage.setItem("title" + pos, "attraction ID: " + attr['id'] + "\nattraction name: " + attr['name'] + "\nposition: (" + attr['x'] + "," + attr['y'] + ")");
                    markAttractionOfMediumPath(pos);

            })
        }

        if(track['length']==3) {
        idOfLong = track['id'];
        }
    });
    getRequestAttractions(markAttractionsOfMediumPath_left);

}

function markAttractionsOfMediumPath_left(attractionsJSON){

    attractionsJSON.forEach(function (attr) {

        let pos = {lat: attr['x'], lng: attr['y']};
        let pos2 = {lat: (attr['x']).toFixed(8), lng: (attr['y']).toFixed(8)};

        let lats=pointsOfShort.map(function (x){return (x.lat)});
        let lngs=pointsOfShort.map(function (x){return (x.lng)});
        let firstBool = lats.includes(pos2.lat);
        let secondBool = lngs.includes(pos2.lng);
        // alert(lats.length);
         if(!(firstBool && secondBool)){
             // alert("ad");
            localStorage.setItem("title" + pos, "attraction ID: " + attr['id'] + "\nattraction name: " + attr['name'] + "\nposition: (" + attr['x'] + "," + attr['y'] + ")");
            markAttractionElse(pos);
        }
    });
}

function listenerForMappo(){
        var finishBTN = document.getElementById('finish_reg_med');
        finishBTN.addEventListener('click', function() {

        //     let the_point = {
        // x: 31.262644482198,
        // y: 34.8007766759185};
        //         addPointToTrackRequest(the_point,idOfMedium);
        //         addPointToTrackRequest(the_point,idOfLong);
            pointsOfPath.forEach(function (point) {
                let the_point = {x: point.lat , y: point.lng};
                addPointToTrackRequest(the_point,idOfMedium);
                addPointToTrackRequest(the_point,idOfLong);
            });

            window.location.href='/edit_path';
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
        addEditListenerr(marker);
        return marker;
}

function markAttractionElse(pos){
    let the_title=localStorage.getItem("title"+pos);
        let marker = new google.maps.Marker({
          position: pos,
          map: map,
          title:the_title
        });
        marker.setMap(map);
        addEditListenerr(marker);
        return marker;
}

function initAttractionsMarkersOfMediumPath() {
    getRequestTracks(markAttractionsOfMediumPaths);
}


function getRequestTracks(funcOnTrack){
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    serverRequest("GET", funcOnTrack, 'http://10.0.0.4:12344/managementsystem/track/?format=json');
}

function addPointToTrackRequest(point_to_add,track_id){
    alert("trackos blatikus");
    serverRequest("PUT", function noop(dummy){}, 'http://10.0.0.4:12344/managementsystem/track/'+track_id+"/add",
        JSON.stringify(point_to_add));
}