let the_length = 0 ;

function funcToGetTrackID(tracksJSON){
    alert("aaaa");
    tracksJSON.forEach(function (track) {
        alert("d "+ the_length);
        if(track['length']==the_length) {
            alert("d");
            deleteRequestTrack(track['id']);
            window.location.href='/main';
        }
    });
}

window.onload = function () {
    let path_length = document.getElementById("write_path_length");

    var deleteTrackBTN = document.getElementById('delete_chosen_path');
    deleteTrackBTN.addEventListener('click', function() {

        let length = path_length.value;
        if(length == "1"){
            the_length=1;
            getRequestTracks(funcToGetTrackID);
           // alert("alerto");
        }
        if(length == "2"){
            the_length=2;
            getRequestTracks(funcToGetTrackID);
        }
        if(length == "3"){
            the_length=3;
            getRequestTracks(funcToGetTrackID);
        }
    });

};



function getRequestTracks(funcOnTrack){
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    alert("alerddto");
    serverRequest("GET", funcOnTrack, 'http://10.0.0.4:12344/managementsystem/track/?format=json');
    alert("alerddto");
}

function deleteRequestTrack(id){
    alert("delitos");
    serverRequest("DELETE", function noop(dummy){}, 'http://10.0.0.4:12344/managementsystem/track/'+id+'/');
}