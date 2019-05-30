let info_txt;
var attr_for_editing;
var helperVar;
var helperVarVid;


window.onload = function () {
    getRequestInfo(func_to_show_info);
    initializeBTNsFunctionality();
    localFileVideoPlayer();
};

function initializeBTNsFunctionality(){
    let vid_title = document.getElementById("vid_title");
    let pic_title = document.getElementById("pic_title");
    let pic_input = document.getElementById("picInput");
    let pic_output = document.getElementById("output");
    let vid_itself = document.getElementById("vid_itself");
    // let vid_input = document.getElementById("video_input");
    let vid_uploadBTN = document.getElementById("upvidBTN");

    let want_upvid = document.getElementById("add_vid_info");
    let want_upic = document.getElementById("add_pic_info");


    want_upic.addEventListener('click',function () {

		pic_title.style.display = '';
		pic_input.style.display = '';
		pic_output.style.display = '';
		vid_title.style.display = 'none';
		vid_itself.style.display = 'none';
		vid_uploadBTN.style.display = 'none';

	});

    want_upvid.addEventListener('click',function () {

		pic_title.style.display = 'none';
		pic_input.style.display = 'none';
		pic_output.style.display = 'none';
		vid_title.style.display = '';
		vid_itself.style.display = '';
		vid_uploadBTN.style.display = '';
	});
}


function doVideo(){
    	let vid_input = document.getElementById('video_input');
        vid_input.click();
}

function func_to_show_info(infoJSON) {
    infoJSON.forEach(function (info) {
        info_txt = info['info'];
    });
    let txt = document.getElementById('subject');
    txt.value=info_txt;
}

function clearText(){
    let txt = document.getElementById('subject');
    txt.value="";
}

function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
	image.src = URL.createObjectURL(element.files[0]);

    helperVar="";

  var file = element.files[0];
  var reader = new FileReader();
  reader.onloadend = function() {
   helperVar = reader.result
  };

  reader.readAsDataURL(file);
}

function sendInfo(){
    let txt = document.getElementById('subject').value;
    let inf = {info:txt};
    postRequestInfo(inf);
    window.location.href ='/main';
}

function getRequestInfo(func){
    // the server port and my ip
    serverRequest("GET", func, 'http://'+ip+':12344/managementsystem/info/?format=json');
}

function postRequestInfo(info){
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/info/',
        JSON.stringify(info));
}


$('document').ready(function(){
	$('input[type="text"], input[type="email"], textarea').focus(function(){
		var background = $(this).attr('id');
		$('#' + background + '-form').addClass('formgroup-active');
		$('#' + background + '-form').removeClass('formgroup-error');
	});
	$('input[type="text"], input[type="email"], textarea').blur(function(){
		var background = $(this).attr('id');
		$('#' + background + '-form').removeClass('formgroup-active');
	});

function errorfield(field){
	$(field).addClass('formgroup-error');
	console.log(field);
}

$("#waterform").submit(function() {
	var stopsubmit = false;

if($('#name').val() == "") {
	errorfield('#name-form');
	stopsubmit=true;
}
if($('#email').val() == "") {
	errorfield('#email-form');
	stopsubmit=true;
}
  if(stopsubmit) return false;
});

});



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