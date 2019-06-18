var helperVar;
var helperVarVid;
let vidName = "";

function uploadVideoBTNclick() {
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
        document.getElementById('nameOfVid').innerText = file.name;
        vidName = file.name;
    };
    let inputNode = document.querySelector('input');
    inputNode.addEventListener('change', playSelectedFile, false);
}


window.onload = function () {
    localStorage.setItem("whereToGoInGame",'/add_game');
    let attr_name = document.getElementById("attr_name");
    let attr_name_english = document.getElementById("attr_name_english");
    let subt = document.getElementById("subt");
    let subt_english = document.getElementById("subt_english");

    let hebrewBTN = document.getElementById("hebrewBTN");
    let englishBTN = document.getElementById("englishBTN");

    hebrewBTN.addEventListener('click', function () {
        attr_name.style.display = "";
        subt.style.display = "";
        attr_name_english.style.display = "none";
        subt_english.style.display = "none";

    });

    englishBTN.addEventListener('click', function () {
        attr_name.style.display = "none";
        subt.style.display = "none";
        attr_name_english.style.display = "";
        subt_english.style.display = "";
    });

    initializingButtonsWithFunctionality();

    localFileVideoPlayer();

};

function initializingButtonsWithFunctionality() {

    let continueBTN = document.getElementById('continueBTN');
    continueBTN.addEventListener('click', function () {
        saveAndProceedToAttractionInfo();
    });

    let submitBTN = document.getElementById('submit_btn_add_attr');
    submitBTN.addEventListener('click', function () {
        submitAttractionWithoutInfo();
    });
}


function submitAttractionWithoutInfo() {

    let addedPoint = JSON.parse(localStorage.getItem("addedPoint"));
    let vidArr = 'null';
    let lat = addedPoint.lat;
    let lang = addedPoint.lng;
    if (helperVarVid != undefined) {
        vidArr = "hello";
        sendLongBase64Parts(helperVarVid);
        // window.location.href = '/add_game';
    }
    let attraction_to_send = {
        name: document.getElementById("attr_name").value + ";;" + document.getElementById("attr_name_english").value
        , x: lat, y: lang
        , description: ";;"
        //, script: document.getElementById("subt").value + ";;" + document.getElementById("subt_english").value
        , picturesURLS: 'null', videosURLS: vidArr
    };

    localStorage.setItem("" + attraction_to_send.name + "_vid", document.getElementById('nameOfVid').innerText);
    localStorage.setItem("name_for_add_aq", attraction_to_send.name);
    localStorage.setItem("desc_for_add_aq", attraction_to_send.description);
    postRequestAttraction(attraction_to_send);
    window.location.href = '/add_game';
}

function saveAndProceedToAttractionInfo() {

    let addedPoint = JSON.parse(localStorage.getItem("addedPoint"));
    let lat = addedPoint.lat;
    let vidArr = 'null';
    if (helperVarVid != undefined) {
        vidArr = "hello";
        sendLongBase64Parts(helperVarVid);
    }
    let lang = addedPoint.lng;
    let name = document.getElementById("attr_name").value + ";;" + document.getElementById("attr_name_english").value;
    localStorage.setItem("" + name + "_vid", document.getElementById('nameOfVid').innerText);
    let x = lat;
    let y = lang;
    //localStorage.setItem("script", JSON.stringify(document.getElementById("subt").value + ";;" + document.getElementById("subt_english").value));
    localStorage.setItem("x", JSON.stringify(x));
    localStorage.setItem("y", JSON.stringify(y));
    localStorage.setItem("vidArr", JSON.stringify(vidArr));
    localStorage.setItem("name_for_add_aq", name);
    localStorage.setItem("desc_for_add_aq", "");
    window.location.href = '/attr_info';

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

// function postRequestAttractionSync(attraction) {
//     syncServerRequest("POST", function noop(dummy) {
//         }, 'http://' + ip + ':12344/managementsystem/attraction/',
//         JSON.stringify(attraction));
// }


