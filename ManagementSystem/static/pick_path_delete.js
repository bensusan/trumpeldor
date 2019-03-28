let the_length = 0 ;

function funcToGetTrackID(tracksJSON){
    tracksJSON.forEach(function (track) {
        if(track['length']==the_length) {
            alert("wat");
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
    // the server port and my ip
    alert("alerddto");
    serverRequest("GET", funcOnTrack, 'http://'+ip+':12344/managementsystem/track/?format=json');
}

function deleteRequestTrack(id){
    alert("delitos");
    serverRequest("DELETE", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/track/'+id+'/');
}