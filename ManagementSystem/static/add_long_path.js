let short_path_points_for_long = JSON.parse(localStorage.getItem("the_points_of_the_short_path"));
let medium_path_points_for_long = JSON.parse(localStorage.getItem("the_points_of_the_medium_path"));
let the_path_points_for_long_lat = [];
let the_path_points_for_long_lng = [];
let the_path_points_for_long = [];

let curPosClicked;


var str_of_points="";
let pointsOfPath = [];

function initMapAndAttractionsss(){

    str_of_points="";
    pointsOfPath = [];
    let j;
    short_path_points_for_long = JSON.parse(localStorage.getItem("the_points_of_the_short_path"));
    medium_path_points_for_long = JSON.parse(localStorage.getItem("the_points_of_the_medium_path"));
    // let the_path_points_for_long = medium_path_points_for_long.push(short_path_points_for_medium);
    the_path_points_for_long = [];
    for(j=0;j<short_path_points_for_long.length;j++)
    {
        the_path_points_for_long.push(short_path_points_for_long[j]);
    }
    for(j=0;j<medium_path_points_for_long.length;j++)
    {
        the_path_points_for_long.push(medium_path_points_for_long[j]);
    }

    the_path_points_for_long_lat = [];
    the_path_points_for_long_lng = [];

    let i;
    for(i=0;i<the_path_points_for_long.length;i++)
    {
        the_path_points_for_long_lat.push(the_path_points_for_long[i].lat);
        the_path_points_for_long_lng.push(the_path_points_for_long[i].lng);
    }
    document.getElementById("things_to_fix_long").innerHTML = "need to fix: if we click on to points and then on the 'add' button it adds both of them." ;

    getRequestAttractions(markAttractionsOfLongPath);
    initMapp();
    initAttractionsMarkersOfLongPath();
}

  function addEditListenerr(m) {

      m.addListener('click', function() {
          curPosClicked=m.position;
        var addToPathBTN = document.getElementById('add_reg_to_path_long');
        addToPathBTN.addEventListener('click', function() {
            if(pointsOfPath.indexOf(m.position)==-1 && curPosClicked==m.position)
            {
                pointsOfPath.push(m.position);
                str_of_points=str_of_points+m.position+"<br />";
            }
            // alert(str_of_points);
            document.getElementById("showing_added_points_long").innerHTML = str_of_points ;
           // alert("point been added! now its: "+ pointsOfPath.toString());
        });
  });
  }

function initMapp() {
     map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: {lat: 31.262860, lng: 34.801753}
    });

   //initAttractionsMarkersOfLongPath();

    listenerForMappo();
   // initPoints();

}

function getRequestLongPath(funcOnLongPath){
    // the server port and my ip
    serverRequest("GET", funcOnLongPath, 'http://10.0.0.4:12344/managementsystem/track/3/?format=json');
}

function postRequestLongPath(long_path){
    alert("long_blatos");
    serverRequest("POST", function noop(dummy){}, 'http://10.0.0.4:12344/managementsystem/track/3/',
        JSON.stringify(long_path));
}


function markAttractionsOfLongPath(attractionsJSON){

    attractionsJSON.forEach(function (attr) {

        let pos = {lat: attr['x'], lng: attr['y']};
        let lats=the_path_points_for_long_lat.map(function (x){return x.toFixed(8)});
        let lngs=the_path_points_for_long_lng.map(function (x){return x.toFixed(8)});
        let firstBool = lats.includes((pos.lat).toFixed(8));
        let secondBool = lngs.includes((pos.lng).toFixed(8));
        if(firstBool && secondBool) {
            // alert("if point in:"+lats.includes((pos.lat).toFixed(8)) +lngs.includes((pos.lng).toFixed(8)));
            localStorage.setItem("title" + pos, "attraction ID: " + attr['id'] + "\nattraction name: " + attr['name'] + "\nposition: (" + attr['x'] + "," + attr['y'] + ")");
            markAttractionOfLongPath(pos);
        }
        else{
            localStorage.setItem("title" + pos, "attraction ID: " + attr['id'] + "\nattraction name: " + attr['name'] + "\nposition: (" + attr['x'] + "," + attr['y'] + ")");
            markAttractionElse(pos);
        }
    });
}

function listenerForMappo(){

        var finishBTN = document.getElementById('finish_reg_long');
        finishBTN.addEventListener('click', function() {
            localStorage.setItem("the_points_of_the_long_path", JSON.stringify(pointsOfPath));
            let arrShow = shitFuncToDelete(the_path_points_for_long,pointsOfPath);
            localStorage.setItem("the_points_of_the_finish_path", JSON.stringify(arrShow));
            // let short_to_send = {length:1,points:pointsOfPath};
            // let medium_to_send = {length:2,points:pointsOfPath};
            // let long_to_send = {length:3,points:pointsOfPath};
            // postRequestShortPath(short_to_send);
            // postRequestMediumPath(medium_to_send);
            // postRequestLongPath(long_to_send);

//the_points_of_the_short_path

            window.location.href='/edit_path';
        });
}

function markAttractionOfLongPath(pos){
    let the_title=localStorage.getItem("title"+pos);
        let marker = new google.maps.Marker({
          position: pos,
          map: map,
          title:the_title
          ,icon: {
                url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
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

function initAttractionsMarkersOfLongPath() {
    getRequestAttractions(markAttractionsOfLongPath);
}

function shitFuncToDelete(arr1,arr2) {
    let j;
    for(j=0;j<arr1.length;j++)
    {
        arr2.push(arr1[j]);
    }

    return arr2;

}
