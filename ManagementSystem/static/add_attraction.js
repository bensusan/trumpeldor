// alert(localStorage.getItem("addedPoint"));


var suki;
var sukiVid;

var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};

function doVideo(){
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
    }

    function showDataCollected() {


        let addedPoint = JSON.parse(localStorage.getItem("addedPoint"));
        // alert("is what: "+ addedPoint.lat +", " + addedPoint.lng + ", "+ (typeof addedPoint.lng));
        // alert("2!");
        // currPoints.push(addedPoint);
        let lat = addedPoint.lat;
        let picArr=[];
        let vidArr=[];
        if(suki!=undefined){picArr.push(suki);}
        if(sukiVid!=undefined){vidArr.push(sukiVid);}
        let lang = addedPoint.lng;
        let attraction_to_send = {
            name:document.getElementById("attr_name").value
            //,x:31.262860,y:34.801753
            ,x:lat ,y:lang
            ,description:document.getElementById("desc").value
            ,picturesURLS:picArr ,videosURLS:vidArr};
        postRequestAttraction(attraction_to_send);
        localStorage.setItem("name_for_add_aq", attraction_to_send.name);
        localStorage.setItem("desc_for_add_aq", attraction_to_send.description);
        window.location.href='/add_game';
        // window.location.href='/attractions';
        // alert("point:"+localStorage.getItem("addedPoint")+"\n"+
        //     "name:"+document.getElementById("attr_name").value);
    }

    function check(){

    alert("ayooooooooo");

    }




function shit(suk) {
    suki=suk;
    document.getElementById("suka").innerHTML=suki;
    localStorage.setItem("url_of_img",suki);
    // var tmuna = document.getElementById("sukablat");
    // tmuna.src = suki;
}


function shitVid(suk) {
    sukiVid=suk;
    // var tmuna = document.getElementById("sukablat");
    // tmuna.src = suki;
}

function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
    image.style.display="inline";
	image.src = URL.createObjectURL(element.files[0]);

    suki="";

  var file = element.files[0];
  var reader = new FileReader();
  reader.onloadend = function() {
   //alert(reader.result)
   shit(reader.result)
  }

  reader.readAsDataURL(file);
}


function encodeVideoFileAsURL(element) {

    sukiVid="";

  var file = element.files[0];
  var reader = new FileReader();
  reader.onloadend = function() {
   //alert(reader.result)
   shitVid(reader.result)
  };

  reader.readAsDataURL(file);
}