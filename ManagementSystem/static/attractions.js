const Http = new XMLHttpRequest();

let marker_arr = [];
let attr_arr_for_test=[];
let attr_arr_for_test2=[];

function serverRequest(getOrPost, functionOnReady, url, post=null){
    Http.onreadystatechange = function(){
        if(Http.readyState === 4 && Http.status === 200){
            functionOnReady(JSON.parse(Http.responseText));
        }
    };
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
    //alert(window.innerHeight + " "+ window.innerWidth);
    attractionsJSON.forEach(function (attr) {
       attr_arr_for_test2.push(attr);

        let pos = {lat: attr['x'], lng: attr['y']};
        marker_arr.push(pos);
        localStorage.setItem("title"+pos,"attraction ID: "+attr['id']+"\nattraction name: "+attr['name']+"\nposition: ("+attr['x']+","+attr['y']+")");
        markAttraction(pos);
        // var currPoints = JSON.parse(localStorage.getItem("points"));
        // currPoints.push(x.position);
        // localStorage.setItem("points",JSON.stringify(currPoints));


    });
        localStorage.setItem("arr_of_markers",JSON.stringify(marker_arr));
        document.getElementById("points_arr_for_test").value=attr_arr_for_test;


}


function markAttraction(pos){
    let the_title=localStorage.getItem("title"+pos);
        let marker = new google.maps.Marker({
          position: pos,
          map: map,
          title:the_title
          ,icon: {
                url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
                }
        });
        // marker_arr.push(marker);
        marker.setMap(map);
        addEditListener(marker);
        return marker;
}

function getRequestAttractions(funcOnAttractions){
    // the server port and my ip
    serverRequest("GET", funcOnAttractions, 'http://'+ip+':12344/managementsystem/attraction/?format=json');
    //alert("need to remove this alert and fix funcToGetAttraction()!");
}


function initAttractionsMarkers() {
    getRequestAttractions(markAttractions);
}


function postRequestAttraction(attraction){
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/',
        JSON.stringify(attraction));
}


function deleteRequestAttraction(id){
   // alert("blich");
    serverRequest("DELETE", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+id+'/');
}


function sendLongBase64Parts(longBase64) {
    let arrOfParts = longBase64.match(/.{1,100000}/g);
    let counter = 0;
    for (let i = 0; i < arrOfParts.length; i++) {
        postRequestFile(arrOfParts[i]);
        counter++;
    }
    postRequestFile("end of file");
}

function sendLongBase64PartsPic(longBase64) {
    let arrOfParts = longBase64.match(/.{1,100000}/g);
    let counter = 0;
    for (let i = 0; i < arrOfParts.length; i++) {
        postRequestFilePic(arrOfParts[i]);
        counter++;
    }
    postRequestFilePic("end of file");
}

function postRequestFile(file) {
    //   alert("hint blat");
    syncServerRequest("POST", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/file/vid',
        JSON.stringify(file));
}

function postRequestFilePic(file) {
    //   alert("hint blat");
    syncServerRequest("POST", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/file/img',
        JSON.stringify(file));
}