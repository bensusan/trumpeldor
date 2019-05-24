
var helperVar;
var helperVarVid;

var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};

function uploadVideoBTNclick(){
    	let vid_input = document.getElementById('video_input');
        vid_input.click();
}

function localFileVideoPlayer() {
	'use strict';
  let URL = window.URL || window.webkitURL;
  let displayMessage = function (message, isError) {
    let element = document.querySelector('#message');
    element.innerHTML = message;
    element.className = isError ? 'error' : 'info'
  };
  let playSelectedFile = function (event) {
    let file = this.files[0];
    let type = file.type;
    let videoNode = document.querySelector('video');
    let canPlay = videoNode.canPlayType(type);
    if (canPlay === '') canPlay = 'no';
    let message = 'Can play type "' + type + '": ' + canPlay;
    let isError = canPlay === 'no';
    //displayMessage(message, isError)

    if (isError) {
      return
    }

    let fileURL = URL.createObjectURL(file);
    videoNode.src = fileURL;

  };
  let inputNode = document.querySelector('input');
  inputNode.addEventListener('change', playSelectedFile, false);
}


window.onload=function(){
    localFileVideoPlayer();
    };

function showDataCollectedWithout() {

        let addedPoint = JSON.parse(localStorage.getItem("addedPoint"));
        // alert("is what: "+ addedPoint.lat +", " + addedPoint.lng + ", "+ (typeof addedPoint.lng));
        // alert("2!");
        // currPoints.push(addedPoint);
        let lat = addedPoint.lat;
        let vidArr=[];
        if(helperVarVid!=undefined){vidArr.push(helperVarVid);}
        let lang = addedPoint.lng;
        let attraction_to_send = {
            name:document.getElementById("attr_name").value
            //,x:31.262860,y:34.801753
            ,x:lat ,y:lang
            ,description:""
            ,picturesURLS:[] ,videosURLS:vidArr};
        postRequestAttraction(attraction_to_send);
        localStorage.setItem("name_for_add_aq", attraction_to_send.name);
        localStorage.setItem("desc_for_add_aq", attraction_to_send.description);
        window.location.href='/add_game';
        // window.location.href='/attractions';
        // alert("point:"+localStorage.getItem("addedPoint")+"\n"+
        //     "name:"+document.getElementById("attr_name").value);
}

    function showDataCollected() {


        let addedPoint = JSON.parse(localStorage.getItem("addedPoint"));
        // alert("is what: "+ addedPoint.lat +", " + addedPoint.lng + ", "+ (typeof addedPoint.lng));
        // alert("2!");
        // currPoints.push(addedPoint);
        let lat = addedPoint.lat;
        let vidArr=[];
        if(helperVarVid!=undefined){vidArr.push(helperVarVid);}
        let lang = addedPoint.lng;
        let name = document.getElementById("attr_name").value;
        let x = lat;
        let y = lang;
        localStorage.setItem("x",JSON.stringify(x));
        localStorage.setItem("y",JSON.stringify(y));
        localStorage.setItem("vidArr",JSON.stringify(helperVarVid));
        localStorage.setItem("name_for_add_aq", name);
        localStorage.setItem("desc_for_add_aq", "");
        window.location.href='/attr_info';
        // window.location.href='/attractions';
        // alert("point:"+localStorage.getItem("addedPoint")+"\n"+
        //     "name:"+document.getElementById("attr_name").value);
    }

    function check(){

    alert("ayooooooooo");

    }


function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
    image.style.display="inline";
	image.src = URL.createObjectURL(element.files[0]);

    helperVar="";

  var file = element.files[0];
  var reader = new FileReader();
  reader.onloadend = function() {
   //alert(reader.result)
   helperVar = reader.result
  };

  reader.readAsDataURL(file);
}


function encodeVideoFileAsURL(element) {

    helperVarVid="";

  var file = element.files[0];
  var reader = new FileReader();
  reader.onloadend = function() {
   helperVarVid= reader.result
  };

  reader.readAsDataURL(file);
}