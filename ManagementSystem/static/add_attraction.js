var helperVar;
var helperVarVid;

var loadFile = function (event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
};

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

    };
    let inputNode = document.querySelector('input');
    inputNode.addEventListener('change', playSelectedFile, false);
}


window.onload = function () {

    let attr_name = document.getElementById("attr_name");
    let attr_name_english = document.getElementById("attr_name_english");
    let subt = document.getElementById("subt");
    let subt_english = document.getElementById("subt_english");
    let pop = document.getElementById("pop");
    let pop_english = document.getElementById("pop_english");

    let hebrewBTN = document.getElementById("hebrewBTN");
    let englishBTN = document.getElementById("englishBTN");

    hebrewBTN.addEventListener('click', function () {
        attr_name.style.display = "";
        subt.style.display = "";
        pop.style.display = "";
        attr_name_english.style.display = "none";
        subt_english.style.display = "none";
        pop_english.style.display = "none";

    });

    englishBTN.addEventListener('click', function () {
        attr_name.style.display = "none";
        subt.style.display = "none";
        pop.style.display = "none";
        attr_name_english.style.display = "";
        subt_english.style.display = "";
        pop_english.style.display = "";
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

    let lat = addedPoint.lat;
    let vidArr = [];
    if (helperVarVid != undefined) {
        vidArr.push(helperVarVid);
    }
    let lang = addedPoint.lng;
    let attraction_to_send = {
        name: document.getElementById("attr_name").value +";;"+document.getElementById("attr_name_english").value
        //,x:31.262860,y:34.801753
        , x: lat, y: lang
        , description: ""
        , picturesURLS: [], videosURLS: vidArr
    };
    postRequestAttraction(attraction_to_send);
    localStorage.setItem(attraction_to_send.name+"_vid", vidArr);
    localStorage.setItem("name_for_add_aq", attraction_to_send.name);
    localStorage.setItem("desc_for_add_aq", attraction_to_send.description);
    window.location.href = '/add_game';
}

function saveAndProceedToAttractionInfo() {


    let addedPoint = JSON.parse(localStorage.getItem("addedPoint"));
    let lat = addedPoint.lat;
    let vidArr = [];
    if (helperVarVid != undefined) {
        vidArr.push(helperVarVid);
    }
    let lang = addedPoint.lng;
    let name = document.getElementById("attr_name").value +";;"+document.getElementById("attr_name_english").value;
    let x = lat;
    let y = lang;
    localStorage.setItem("x", JSON.stringify(x));
    localStorage.setItem("y", JSON.stringify(y));
    localStorage.setItem("vidArr", JSON.stringify(vidArr));
    localStorage.setItem(name+"_vid", vidArr);
    localStorage.setItem("name_for_add_aq", name);
    localStorage.setItem("desc_for_add_aq", "");
    window.location.href = '/attr_info';
    // window.location.href='/attractions';
    // alert("point:"+localStorage.getItem("addedPoint")+"\n"+
    //     "name:"+document.getElementById("attr_name").value);
}

function check() {

    alert("ayooooooooo");

}


function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
    image.style.display = "inline";
    image.src = URL.createObjectURL(element.files[0]);

    helperVar = "";

    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        //alert(reader.result)
        helperVar = reader.result
    };

    reader.readAsDataURL(file);
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