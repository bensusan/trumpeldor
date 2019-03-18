var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};

window.onload = function () {
var textHintBTN = document.getElementById('add_text_hint');
        textHintBTN.addEventListener('click', function() {

            var textLine = document.getElementById("text_hint_id");
            textLine.style.display = "inline";

            var sendButton = document.getElementById("send_text_hint");
            sendButton.style.display = "inline";

        });

var picHintBTN = document.getElementById('add_pic_hint');
        picHintBTN.addEventListener('click', function() {
            var clickHere = document.getElementById("click_here_label");
            clickHere.style.display = "inline";

            var outpic = document.getElementById("output");
            outpic.style.display = "inline";

            var sendButton = document.getElementById("send_pic_hint");
            sendButton.style.display = "inline";
        });

var vidHintBTN = document.getElementById('add_vid_hint');
        vidHintBTN.addEventListener('click', function() {
            var thevid = document.getElementById("vid_hint_id");
            thevid.style.display = "inline";

            var thevidbrowse = document.getElementById("vid_hint_browse_id");
            thevidbrowse.style.display = "inline";

            var sendButton = document.getElementById("send_vid_hint");
            sendButton.style.display = "inline";
        });

var sendTextHintBTN = document.getElementById('send_text_hint');
    sendTextHintBTN.addEventListener('click', function() {
        getRequestAttractions(hint_funcToGetAttraction);
    });

var sendPicHintBTN = document.getElementById('send_pic_hint');
    sendPicHintBTN.addEventListener('click', function() {

    });

var sendVidHintBTN = document.getElementById('send_vid_hint');
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
            data:document.getElementById("text_hint_id").value
            };
            postRequestHint(textHintToSend,attr['id']);
            window.location.href='/add_hint';
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
    alert("hint was added successfully!");
    // let data=document.getElementById("data").value;
    // let hint_to_send = {
    //         attraction:"" //atraction id needs to be here
    //     ,kind:
    //     ,data:
    // };
        // postRequestHint(hint_to_send);

    window.location.href='/attractions';
}

function postRequestHint(the_hint,attr_id){
    alert("hint blat");
    serverRequest("POST", function noop(dummy){}, 'http://10.0.0.7:12344/managementsystem/attraction/'+
        attr_id+'/hint/',
        JSON.stringify(the_hint));
}