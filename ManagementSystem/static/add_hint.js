var str;
var helperVar;
var helperVarVid;

var loadFile = function (event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
};


function funcForExistingHints(attractionsJSON) {

    let name = localStorage.getItem("name_for_add_aq");
    let desc = localStorage.getItem("desc_for_add_aq");
    // alert("in get name! "+"of the origin : " + lat + " , " + lng);
    attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description: attr['description']};
        if (p.name === name && p.description === desc) {
            getRequestHints(loadStringOfInnerHTMLWithHints, attr['id']);
        }
    });
}

function loadStringOfInnerHTMLWithHints(hintsJSON) {
    str = "";
    let imageCounter = 1;
    let videoCounter = 1;

    hintsJSON.forEach(function (hint) {

        let dataOfHint = hint['data'];
        if (dataOfHint.substring(0, 16) == 'data:application')
            str = str + " data: " + "media" + imageCounter + "<br />";
        else {
            if (hint['data'].substring(0, 10) == 'data:video')
                str = str + " data: " + "VideoMedia" + videoCounter + "<br />";
            else
                str = str + " data: " + hint['data'] + "<br />";
        }


        // alert(str);

        var output = document.getElementById("result");
        var outputVideo = document.getElementById("resultVideos");

        if (hint['data'].substring(0, 16) == 'data:application') {
            imageCounter++;
            var img = document.createElement("img");
            img.src = dataOfHint;
            img.className = 'thumbnail';
            var div = document.createElement("div");
            div.appendChild(img);


            output.insertBefore(div, null);
        }

        if (hint['data'].substring(0, 10) == 'data:video') {
            videoCounter++;
            var vid = document.createElement("video");
            vid.src = dataOfHint;
            vid.className = 'thumbnail';
            var div = document.createElement("div");
            vid.autoplay = true;
            div.appendChild(vid);

            outputVideo.insertBefore(div, null);
        }

    });
    document.getElementById("existing_hints").innerHTML = str;
    document.getElementById("existing_hints").style.fontWeight = 'bold';
    document.getElementById("existing_hints").style.fontFamily = 'david';
    document.getElementById("existing_hints").style.fontSize = '24px';
}


function getRequestHints(funcOnHints, attr_id) {
    serverRequest("GET", funcOnHints, 'http://' + ip + ':12344/managementsystem/attraction/' + attr_id +
        '/hint/?format=json');
}

window.onload = function () {


    getRequestAttractions(funcForExistingHints);
    initializeBTNsFunctionality();

    localFileVideoPlayer();

};

function initializeBTNsFunctionality() {
    var textHintBTN = document.getElementById('add_text_hint');
    var textLineEnglish = document.getElementById('text_hint_id_english');
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

    textHintBTN.addEventListener('click', function () {
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
        window.scrollTo(0, document.body.scrollHeight);


        let hebrewBTN = document.getElementById("hebrewBTN");
        let englishBTN = document.getElementById("englishBTN");

        hebrewBTN.addEventListener('click', function () {
            textLine.style.display = "";
            textLineEnglish.style.display = "none";
        });

        englishBTN.addEventListener('click', function () {
            textLine.style.display = "none";
            textLineEnglish.style.display = "";
        });

    });

    var picHintBTN = document.getElementById('add_pic_hint');
    picHintBTN.addEventListener('click', function () {
        clickHere.style.display = "inline";
        picDesc.style.display = "inline";
        outpic.style.display = "inline";
        upload_pic_title.style.display = "inline";
        sendButtonPic.style.display = "inline";
        textLine.style.display = "none";
        textLineEnglish.style.display = "none";
        sendButtonTxt.style.display = "none";
        thevid.style.display = "none";
        vidDesc.style.display = "none";
        thevidbrowse.style.display = "none";
        sendButtonVid.style.display = "none";
        window.scrollTo(0, document.body.scrollHeight);

    });

    var vidHintBTN = document.getElementById('add_vid_hint');
    vidHintBTN.addEventListener('click', function () {
        thevid.style.display = "inline";
        vidDesc.style.display = "inline";
        thevidbrowse.style.display = "inline";
        sendButtonVid.style.display = "inline";
        textLine.style.display = "none";
        textLineEnglish.style.display = "none";
        sendButtonTxt.style.display = "none";
        clickHere.style.display = "none";
        picDesc.style.display = "none";
        outpic.style.display = "none";
        sendButtonPic.style.display = "none";
        upload_pic_title.style.display = "none";
        window.scrollTo(0, document.body.scrollHeight);

    });

    sendTextHintBTN.addEventListener('click', function () {
        getRequestAttractions(getTheNeededAttractionIdToSendItOnThePostRequest);
    });

    sendPicHintBTN.addEventListener('click', function () {
        sendImageHint();
    });

    sendVidHintBTN.addEventListener('click', function () {
        sendVideoHint();
    });
}


function getTheNeededAttractionIdToSendItOnThePostRequest(attractionsJSON) {
    let name = localStorage.getItem("name_for_add_aq");
    let desc = localStorage.getItem("desc_for_add_aq");
    // alert("in get name! "+"of the origin : " + lat + " , " + lng);
    attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description: attr['description']};
        // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if (p.name === name && p.description === desc) {
            var textHintToSend = {
                attraction: attr,
                kind: 'HT',
                data: document.getElementById("text_hint_id").value + ";;" + document.getElementById("text_hint_id_english").value,
                description: ""
            };
            postRequestHint(textHintToSend, attr['id']);
            window.location.href = '/add_hint';
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
    window.location.href = '/attractions';
}

function postRequestHint(the_hint, attr_id) {
    serverRequest("POST", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/attraction/' +
        attr_id + '/hint/',
        JSON.stringify(the_hint));
}


function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(element.files[0]);

    helperVar = "";

    var file = element.files[0];
    var blob = file.slice();
    var reader = new FileReader();
    reader.onloadend = function () {
        helperVar = reader.result
    }

    reader.readAsDataURL(blob);       //file instead of blob
}

function encodeVideoFileAsURL(element) {

    helperVarVid = "";

    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        helperVarVid = reader.result
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
        let p = {name: attr['name'], description: attr['description']};
        // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if (p.name === name && p.description === desc) {

            let the_hint = {
                attraction: attr,
                kind: "HP",
                data: helperVar,
                description: document.getElementById("pic_hint_description").value
            };
            let attr_id = attr['id'];
            postRequestHint(the_hint, attr_id);
            window.location.href = '/add_hint';
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
        let p = {name: attr['name'], description: attr['description']};
        // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if (p.name === name && p.description === desc) {

            let the_hint = {
                attraction: attr,
                kind: "HV",
                data: helperVarVid,
                description: document.getElementById("vid_hint_description").value
            };
            let attr_id = attr['id'];
            postRequestHint(the_hint, attr_id);
            window.location.href = '/add_hint';
        }

    });
}