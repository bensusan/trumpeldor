var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};

var str;

function funcForExistingHints(attractionsJSON){

    let name = localStorage.getItem("name_for_add_aq");
        let desc = localStorage.getItem("desc_for_add_aq");
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
        attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description:attr['description']};
        if(p.name===name && p.description===desc)
        {
            getRequestHints(hints_func,attr['id']);
        }
        });
}

function hints_func(hintsJSON) {
        str="";
        hintsJSON.forEach(function (hint) {
            str=str+"id: "+hint['id'] +", data: "+ hint['data']+"<br />";
            // alert(str);
        });
        document.getElementById("existing_hints").innerHTML = str ;
}

function getRequestHints(funcOnHints,attr_id){
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    serverRequest("GET", funcOnHints, 'http://'+ip+':12344/managementsystem/attraction/'+ attr_id+
        '/hint/?format=json');
    //alert("need to remove this alert and fix funcToGetAttraction()!");
}

window.onload = function () {

    getRequestAttractions(funcForExistingHints);
var textHintBTN = document.getElementById('add_text_hint');
var textLine = document.getElementById("text_hint_id");
var sendButtonTxt = document.getElementById("send_text_hint");
var upload_pic_title = document.getElementById("upload_title");
var clickHere = document.getElementById("file");
var picDesc = document.getElementById("pic_hint_description");
var outpic = document.getElementById("output");
var sendButtonPic = document.getElementById("send_pic_hint");
var thevid = document.getElementById("vid_hint_id");
var vidDesc = document.getElementById("vid_hint_description");
var thevidbrowse = document.getElementById("vid_hint_browse_id");
var sendButtonVid = document.getElementById("send_vid_hint");
var sendTextHintBTN = document.getElementById('send_text_hint');
var sendPicHintBTN = document.getElementById('send_pic_hint');
var sendVidHintBTN = document.getElementById('send_vid_hint');

        textHintBTN.addEventListener('click', function() {
            textLine.style.display = "inline";
            sendButtonTxt.style.display = "inline";
             clickHere.style.display = "none";
            picDesc.style.display = "none";
            outpic.style.display = "none";
            sendButtonPic.style.display = "none";
            thevid.style.display = "none";
            vidDesc.style.display = "none";
            thevidbrowse.style.display = "none";
            sendButtonVid.style.display = "none";
            upload_pic_title.style.display = "none";
        });

var picHintBTN = document.getElementById('add_pic_hint');
        picHintBTN.addEventListener('click', function() {
            clickHere.style.display = "inline";
            picDesc.style.display = "inline";
            outpic.style.display = "inline";
            upload_pic_title.style.display = "inline";
            sendButtonPic.style.display = "inline";
             textLine.style.display = "none";
            sendButtonTxt.style.display = "none";
            thevid.style.display = "none";
            vidDesc.style.display = "none";
            thevidbrowse.style.display = "none";
            sendButtonVid.style.display = "none";
        });

var vidHintBTN = document.getElementById('add_vid_hint');
        vidHintBTN.addEventListener('click', function() {
            thevid.style.display = "inline";
            vidDesc.style.display = "inline";
            thevidbrowse.style.display = "inline";
            sendButtonVid.style.display = "inline";
            textLine.style.display = "none";
            sendButtonTxt.style.display = "none";
             clickHere.style.display = "none";
            picDesc.style.display = "none";
            outpic.style.display = "none";
            sendButtonPic.style.display = "none";
            upload_pic_title.style.display = "none";

        });

    sendTextHintBTN.addEventListener('click', function() {
        getRequestAttractions(hint_funcToGetAttraction);
    });

    sendPicHintBTN.addEventListener('click', function() {

    });

    sendVidHintBTN.addEventListener('click', function() {

    });

        localFileVideoPlayer();

};

function hint_funcToGetAttraction(attractionsJSON) {
        let name = localStorage.getItem("name_for_add_aq");
        let desc = localStorage.getItem("desc_for_add_aq");
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
        attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description:attr['description']};
       // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if(p.name===name && p.description===desc)
        {
            var textHintToSend = {
            attraction:attr,
            kind:'HT',
            data:document.getElementById("text_hint_id").value,
                description:""
            };
            postRequestHint(textHintToSend,attr['id']);
            window.location.href='/add_hint_edit';
        }

      });

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


function finishHint() {
    window.location.href='/pick_hint_edit';

}

function postRequestHint(the_hint,attr_id){
    //alert("hint blat");
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+
        attr_id+'/hint/',
        JSON.stringify(the_hint));
}


var suki;
var sukiVid;


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


function sendImageHint() {
    getRequestAttractions(funcToSendImage);
}

function funcToSendImage(attractionsJSON) {
     let name = localStorage.getItem("name_for_add_aq");
        let desc = localStorage.getItem("desc_for_add_aq");
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
        attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description:attr['description']};
       // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if(p.name===name && p.description===desc)
        {
            let diskit = document.getElementById("pic_hint_description").value;
            // alert(diskit);
            let the_hint = {attraction: attr, kind: "HP", data:suki,description:diskit};
            let attr_id = attr['id'];
            postRequestHint(the_hint,attr_id);
            window.location.href='/add_hint_edit';
        }

    });
}


function sendVideoHint() {
    getRequestAttractions(funcToSendVideo);
}

function funcToSendVideo(attractionsJSON) {
     let name = localStorage.getItem("name_for_add_aq");
        let desc = localStorage.getItem("desc_for_add_aq");
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
        attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description:attr['description']};
       // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if(p.name===name && p.description===desc)
        {

            let the_hint = {attraction: attr, kind: "HV", data:sukiVid,description:document.getElementById("vid_hint_description").value};
            let attr_id = attr['id'];
            postRequestHint(the_hint,attr_id);
            window.location.href='/add_hint_edit';
        }

    });
}