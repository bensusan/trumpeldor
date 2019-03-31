
let curPosClicked;

var str_of_points="";
let pointsOfPath = [];
let pointsOfShort = [];
let pointsOfMedium = [];
let fullShortPoints = [];
let idOfShort = 0;
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
            if(prev_m!=1) {
              prev_m.setIcon("http://maps.google.com/mapfiles/ms/icons/red-dot.png");
          }
          //alert("sda");
          m.setIcon("http://maps.google.com/mapfiles/ms/icons/pink-dot.png");
          prev_m=m;
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
            var border = document.getElementById("border_of_points");
            border.style.display = "block";
            document.getElementById("showing_added_points").innerHTML = str_of_points;
            document.getElementById("showing_added_points").style.fontWeight = 'bold';
           // alert("point been added! now its: "+ pointsOfPath.toString());
        });

        var deleteFromPathBTN = document.getElementById('delete_from_path_med');
        deleteFromPathBTN.addEventListener('click', function() {
                //let point_to_delete = {lat: m.position.lat(), lng: m.position.lng()};
                let point_to_delete2 = {lat: m.position.lat().toFixed(10), lng: m.position.lng().toFixed(10)};
                fullShortPoints.forEach(function (med_point) {
                   // alert(med_point['x'] +","+med_point['y'] +"\n"+point_to_delete2.lat+","+point_to_delete2.lng);
                     if((med_point['x'].toFixed(10) == point_to_delete2.lat)  &&
                         (med_point['y'].toFixed(10) == point_to_delete2.lng))
                     {
                         deletePointFromTrackRequest(med_point['id'],idOfShort);
                    }
                });
            window.location.href='/edit_short_path';

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
                    let pos = {lat: attr['x'], lng: attr['y']};
                    let pos2 = {lat: (attr['x']).toFixed(8), lng: (attr['y']).toFixed(8)};

                    pointsOfMedium.push(pos2);
                    // localStorage.setItem("title" + pos, "attraction ID: " + attr['id'] + "\nattraction name: " + attr['name'] + "\nposition: (" + attr['x'] + "," + attr['y'] + ")");
                    // markAttractionOfMediumPath(pos);
            })
        }

        if(track['length']==1)
        {
            idOfShort = track['id'];
            let points_of_track = track['points'];
            points_of_track.forEach(function (attr) {
                    let pos = {lat: attr['x'], lng: attr['y']};
                    let pos2 = {lat: (attr['x']).toFixed(8), lng: (attr['y']).toFixed(8)};
                    pointsOfShort.push(pos2);
                    fullShortPoints.push(attr);
                    localStorage.setItem("title" + pos, "attraction ID: " + attr['id'] + "\nattraction name: " + attr['name'] + "\nposition: (" + attr['x'] + "," + attr['y'] + ")");
                    markAttractionOfShortPath(pos);
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

            getRequestAttractions(needThisToGetPointsIDs);

        });
}

function needThisToGetPointsIDs(attractionsJSON) {

    attractionsJSON.forEach(function (attr) {
        let attr_point = {x: (attr['x']).toFixed(10) , y: (attr['y']).toFixed(10)};
        let attr_id = attr['id'];
        pointsOfPath.forEach(function (point) {
                let the_point = {x: (point.lat).toFixed(10) , y: (point.lng).toFixed(10)};
                // let bolia = attr_point == the_point;
                // alert("attr: "+ attr_point.x +","+ attr_point.y +"\npont: "+the_point.x +","+the_point.y+"\n"+bolia);
                if((attr_point.x == the_point.x)  &&  (attr_point.y == the_point.y) ){
                //   alert("bazinga!");
                    addPointToTrackRequest(attr_id,idOfShort);

                }

            });
    });
    window.location.href='/edit_short_path';
    //window.location.href='/edit_path';
}

function executeAsynchronously(functions, timeout) {
  for(let i = 0; i < functions.length; i++) {
    setTimeout(functions[i], timeout);
  }
}

function markAttractionOfShortPath(pos){
    let the_title=localStorage.getItem("title"+pos);
        let marker = new google.maps.Marker({
          position: pos,
          map: map,
          title:the_title
          ,icon: {
                url: "http://maps.google.com/mapfiles/ms/icons/purple-dot.png"
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
          ,icon: {
                url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
                }
        });
        marker.setMap(map);
        addEditListenerr(marker);
        return marker;
}

function initAttractionsMarkersOfMediumPath() {
    getRequestTracks(markAttractionsOfMediumPaths);
}


function getRequestTracks(funcOnTrack){
    // the server port and my ip
    serverRequest("GET", funcOnTrack, 'http://'+ip+':12344/managementsystem/track/?format=json');
}

function addPointToTrackRequest(id_of_point_to_add,track_id){
    //alert("trackos blatikus");
    serverRequest("PUT", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/track/'+track_id+'/add',
        JSON.stringify(id_of_point_to_add));
}

function deletePointFromTrackRequest(id_of_point_to_del,track_id){
   // alert("trackos mohekos");
    serverRequest("PUT", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/track/'+track_id+'/del',
        JSON.stringify(id_of_point_to_del));
}