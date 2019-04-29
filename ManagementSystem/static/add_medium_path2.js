let short_path_points_for_medium = JSON.parse(localStorage.getItem("the_points_of_the_short_path"));
let short_path_points_for_medium_lat = [];
let short_path_points_for_medium_lng = [];
let curPosClicked;

var str_of_points="";
let pointsOfPath = [];

function initMapAndAttractionss(){
    str_of_points="";
    pointsOfPath = [];
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

  function addEditListenerr(m) {

      m.addListener('click', function() {
          curPosClicked=m.position;
        var addToPathBTN = document.getElementById('add_reg_to_path_med');
        addToPathBTN.addEventListener('click', function() {
            if(pointsOfPath.indexOf(m.position)==-1 && curPosClicked==m.position)
            {
                pointsOfPath.push(m.position);
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
            markAttractionElse(pos);
        }
    });
}

function listenerForMappo(){

        var finishBTN = document.getElementById('finish_reg_med');
        finishBTN.addEventListener('click', function() {
            localStorage.setItem("the_points_of_the_medium_path", JSON.stringify(pointsOfPath));
            let arrShow = shitFuncToDelete(short_path_points_for_medium,pointsOfPath);
            alert(arrShow.length);
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
    getRequestAttractions(markAttractionsOfMediumPath);
}

function shitFuncToDelete(arr1,arr2) {
    let j;
    for(j=0;j<arr1.length;j++)
    {
        arr2.push(arr1[j]);
    }

    return arr2;
    
}