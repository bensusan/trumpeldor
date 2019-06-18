let appName;
let aboutApp;
let howToPlay;
var helperVar;

window.onload = function () {
    let sendInfoBTN = document.getElementById("sendInfo");
    sendInfoBTN.addEventListener('click', function () {
        sendInfo();
    });
    let clearInfoBTN = document.getElementById("clear");
    clearInfoBTN.addEventListener('click', function () {
        clearText();
    });
    initLanguageBTNs();
    getRequestInfo(func_to_show_info);
    initializeBTNsFunctionality();
    localFileVideoPlayer();
};

function initLanguageBTNs() {
    let hebrewBTN = document.getElementById("hebrewBTN");
    let englishBTN = document.getElementById("englishBTN");
    let name = document.getElementById("appName");
    let nameEng = document.getElementById("appNameEnglish");
    let about = document.getElementById("aboutApp");
    let aboutEng = document.getElementById("aboutAppEnglish");
    let howto = document.getElementById("howToPlay");
    let howtoEng = document.getElementById("howToPlayEnglish");

    hebrewBTN.addEventListener('click', function () {
        name.style.display = "";
        nameEng.style.display = "none";
        about.style.display = "";
        aboutEng.style.display = "none";
        howto.style.display = "";
        howtoEng.style.display = "none";
    });

    englishBTN.addEventListener('click', function () {
        name.style.display = "none";
        nameEng.style.display = "";
        about.style.display = "none";
        aboutEng.style.display = "";
        howto.style.display = "none";
        howtoEng.style.display = "";
    });
}

function initializeBTNsFunctionality() {
    let vid_title = document.getElementById("vid_title");
    let pic_title = document.getElementById("pic_title");
    let pic_input = document.getElementById("picInput");
    let pic_output = document.getElementById("output");
    let vid_itself = document.getElementById("vid_itself");
    let vid_uploadBTN = document.getElementById("upvidBTN");

    let want_upvid = document.getElementById("add_vid_info");
    let want_upic = document.getElementById("add_pic_info");


    want_upic.addEventListener('click', function () {

        pic_title.style.display = '';
        pic_input.style.display = '';
        pic_output.style.display = '';
        vid_title.style.display = 'none';
        vid_itself.style.display = 'none';
        vid_uploadBTN.style.display = 'none';

    });

    want_upvid.addEventListener('click', function () {

        pic_title.style.display = 'none';
        pic_input.style.display = 'none';
        pic_output.style.display = 'none';
        vid_title.style.display = '';
        vid_itself.style.display = '';
        vid_uploadBTN.style.display = '';
    });
}


function doVideo() {
    let vid_input = document.getElementById('video_input');
    vid_input.click();
}

function func_to_show_info(info) {
    appName = info['app_name'].split(';;');
    aboutApp = info['about_app'].split(';;');
    howToPlay = info['how_to_play'].split(';;');
    let name = document.getElementById('appName');
    let nameEnglish = document.getElementById('appNameEnglish');
    name.value = appName[0];
    nameEnglish.value = appName[1];
    let about = document.getElementById('aboutApp');
    let aboutEnglish = document.getElementById('aboutAppEnglish');
    about.value = aboutApp[0];
    aboutEnglish.value = aboutApp[1];
    let howtoplay = document.getElementById('howToPlay');
    let howtoplayEnglish = document.getElementById('howToPlayEnglish');
    howtoplay.value = howToPlay[0];
    howtoplayEnglish.value = howToPlay[1];
}

function clearText() {
    let name = document.getElementById('appName');
    let nameEnglish = document.getElementById('appNameEnglish');
    let aboutEnglish = document.getElementById('aboutAppEnglish');
    let howtoplayEnglish = document.getElementById('howToPlayEnglish');
    let about = document.getElementById('aboutApp');
    let howtoplay = document.getElementById('howToPlay');
    name.value = "";
    about.value = "";
    howtoplay.value = "";
    nameEnglish.value = "";
    aboutEnglish.value = "";
    howtoplayEnglish.value = "";
}

function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(element.files[0]);

    helperVar = "";

    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        helperVar = reader.result
    };

    reader.readAsDataURL(file);
}

function sendInfo() {
    let name = document.getElementById('appName').value + ';;' + document.getElementById('appNameEnglish').value;
    let about = document.getElementById('aboutApp').value + ';;' + document.getElementById('aboutAppEnglish').value;
    let howToPlay = document.getElementById('howToPlay').value + ';;' + document.getElementById('howToPlayEnglish').value;
    let inf = {app_name: name, about_app: about, how_to_play: howToPlay};
    postRequestInfo(inf);
    window.location.href = '/main';
}

function getRequestInfo(func) {
    // the server port and my ip
    syncServerRequest("GET", func, 'http://' + ip + ':12344/managementsystem/info/?format=json');
}

function postRequestInfo(info) {
    syncServerRequest("POST", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/info/',
        JSON.stringify(info));
}


$('document').ready(function () {
    $('input[type="text"], input[type="email"], textarea').focus(function () {
        var background = $(this).attr('id');
        $('#' + background + '-form').addClass('formgroup-active');
        $('#' + background + '-form').removeClass('formgroup-error');
    });
    $('input[type="text"], input[type="email"], textarea').blur(function () {
        var background = $(this).attr('id');
        $('#' + background + '-form').removeClass('formgroup-active');
    });

    function errorfield(field) {
        $(field).addClass('formgroup-error');
        console.log(field);
    }

    $("#waterform").submit(function () {
        var stopsubmit = false;

        if ($('#name').val() == "") {
            errorfield('#name-form');
            stopsubmit = true;
        }
        if ($('#email').val() == "") {
            errorfield('#email-form');
            stopsubmit = true;
        }
        if (stopsubmit) return false;
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