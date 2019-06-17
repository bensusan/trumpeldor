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
    let i = 1;
    hintsJSON.forEach(function (hint) {

        let dataOfHint = hint['data'];
        if (dataOfHint.substring(0, 16) == 'data:application')
            str = str + " data: " + "media" + imageCounter + "<br />";
        else {
            if (hint['data'].substring(0, 10) == 'data:video')
                str = str + " data: " + "VideoMedia" + videoCounter + "<br />";
            else
                str = str + i + "." + hint['data'].split(';;')[0] + "<br />";
        }
        i += 1;

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
    let hebrewBTN = document.getElementById("hebrewBTN");
    let englishBTN = document.getElementById("englishBTN");
    let textHintBTN = document.getElementById('add_text_hint');
    let textLineEnglish = document.getElementById('text_hint_id_english');
    let textLine = document.getElementById("text_hint_id");
    let sendButtonTxt = document.getElementById("send_text_hint");
    let upload_pic_title = document.getElementById("upload_title");
    let clickHere = document.getElementById("file");
    let picDesc = document.getElementById("pic_hint_description");
    let outpic = document.getElementById("output");
    var thevid = document.getElementById("vid_hint_id");
    let vidDesc = document.getElementById("vid_hint_description");
    var thevidbrowse = document.getElementById("vid_hint_browse_id");
    var sendTextHintBTN = document.getElementById('send_text_hint');
    var sendPicHintBTN = document.getElementById('send_pic_hint');
    var sendVidHintBTN = document.getElementById('send_vid_hint');
    var vidEng = document.getElementById("vid_hint_descriptionEnglish");
    var picEng = document.getElementById("pic_hint_descriptionEnglish");

    textHintBTN.addEventListener('click', function () {
        textLine.style.display = "";
        sendButtonTxt.style.display = "";
        clickHere.style.display = "none";
        picDesc.style.display = "none";
        picEng.style.display = "none";
        outpic.style.display = "none";
        sendPicHintBTN.style.display = "none";
        thevid.style.display = "none";
        vidDesc.style.display = "none";
        vidEng.style.display = "none";
        thevidbrowse.style.display = "none";
        sendVidHintBTN.style.display = "none";
        upload_pic_title.style.display = "none";
        window.scrollTo(0, document.body.scrollHeight);

        hebrewBTN.addEventListener('click', function () {
            picEng.style.display = "none";
            picDesc.style.display = "none";
            vidDesc.style.display = "none";
            vidEng.style.display = "none";
            textLine.style.display = "";
            textLineEnglish.style.display = "none";
        });

        englishBTN.addEventListener('click', function () {
            picEng.style.display = "none";
            picDesc.style.display = "none";
            vidDesc.style.display = "none";
            vidEng.style.display = "none";
            textLine.style.display = "none";
            textLineEnglish.style.display = "";
        });
    });

    var picHintBTN = document.getElementById('add_pic_hint');
    picHintBTN.addEventListener('click', function () {

        clickHere.style.display = "";
        picDesc.style.display = "";
        outpic.style.display = "";
        upload_pic_title.style.display = "";
        sendPicHintBTN.style.display = "";
        textLine.style.display = "none";
        sendButtonTxt.style.display = "none";
        thevid.style.display = "none";
        vidDesc.style.display = "none";
        vidEng.style.display = "none";
        thevidbrowse.style.display = "none";
        sendVidHintBTN.style.display = "none";
        textLineEnglish.style.display = "none";
        window.scrollTo(0, document.body.scrollHeight);
        hebrewBTN.addEventListener('click', function () {
            picEng.style.display = "none";
            picDesc.style.display = "";
            vidDesc.style.display = "none";
            vidEng.style.display = "none";
            textLine.style.display = "none";
            textLineEnglish.style.display = "none";
        });

        englishBTN.addEventListener('click', function () {
            picEng.style.display = "";
            picDesc.style.display = "none";
            vidDesc.style.display = "none";
            vidEng.style.display = "none";
            textLine.style.display = "none";
            textLineEnglish.style.display = "none";
        });
    });

    var vidHintBTN = document.getElementById('add_vid_hint');
    vidHintBTN.addEventListener('click', function () {
        thevid.style.display = "";
        vidDesc.style.display = "";
        thevidbrowse.style.display = "";
        sendVidHintBTN.style.display = "";
        textLine.style.display = "none";
        sendButtonTxt.style.display = "none";
        clickHere.style.display = "none";
        picDesc.style.display = "none";
        picEng.style.display = "none";
        outpic.style.display = "none";
        sendPicHintBTN.style.display = "none";
        upload_pic_title.style.display = "none";
        textLineEnglish.style.display = "none";
        window.scrollTo(0, document.body.scrollHeight);

        hebrewBTN.addEventListener('click', function () {
            picEng.style.display = "none";
            picDesc.style.display = "none";
            vidDesc.style.display = "";
            vidEng.style.display = "none";
            textLine.style.display = "none";
            textLineEnglish.style.display = "none";
        });

        englishBTN.addEventListener('click', function () {
            picEng.style.display = "none";
            picDesc.style.display = "none";
            vidDesc.style.display = "none";
            vidEng.style.display = "";
            textLine.style.display = "none";
            textLineEnglish.style.display = "none";
        });
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
    let pixArr = ["hello"];
    if (helperVar != undefined) {
        // can do it with all pics.. just add loop
        sendLongBase64PartsPic(helperVar);
        window.location.href = '/add_hint';
    }
    attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description: attr['description']};
        // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if (p.name === name && p.description === desc) {

            let the_hint = {
                attraction: attr,
                kind: "HP",
                data: pixArr,
                description: document.getElementById("pic_hint_description").value + ';;' + document.getElementById("pic_hint_descriptionEnglish").value
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
    let vidArr = ["hello"];
    if (helperVarVid != undefined) {
        sendLongBase64Parts(helperVarVid);
    }
    attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description: attr['description']};
        // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if (p.name === name && p.description === desc) {

            let the_hint = {
                attraction: attr,
                kind: "HV",
                data: vidArr,
                description: document.getElementById("vid_hint_description").value + ';;' + document.getElementById("vid_hint_descriptionEnglish").value
            };
            let attr_id = attr['id'];
            postRequestHint(the_hint, attr_id);
            window.location.href = '/add_hint';
        }

    });
}