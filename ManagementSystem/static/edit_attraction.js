var attr_for_editing;
var helperVar;
var helperVarVid;
let arrOfPicsData = [];

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
    let saveEditBTN = document.getElementById("saveEditBTN");
    saveEditBTN.addEventListener('click', function () {
        finishEditingAttraction();
    });
    let deletePointBTN = document.getElementById("delete_point");
    deletePointBTN.addEventListener('click', function () {
        deletePoint();
    });
    getRequestAttractions(getFieldsValuesOfExistingAttraction);
    localFileVideoPlayer();
    initializeTheListOfPicturesToShow();
    // document.getElementById('randomPic').src = "\\trumpeldor\\TripServer\\media\\87a.jpg";
};


function uploadVideoBTNclick() {
    let vid_input = document.getElementById('video_input');
    vid_input.click();
}


function finishEditingAttraction() {
    let attr_after_editing;
    let vidArr = ["hello"];
    if (helperVarVid != undefined) {
        sendLongBase64Parts(helperVarVid);
    } else {
        if (attr_for_editing['videosURLS'] != []) {
            vidArr = [attr_for_editing['videosURLS']];
        } else {
            vidArr = 'null';
        }
    }
    let pixArr = ["hello"];
    if (arrOfPicsData.length != 0) {
        // can do it with all pics.. just add loop
        sendLongBase64PartsPic(arrOfPicsData[0]);
       // window.location.href = '/attractions';
    } else {
        if (attr_for_editing['picturesURLS'].length != 0) {
            pixArr = attr_for_editing['picturesURLS'];
        } else {
            pixArr = 'null';
        }
    }

    attr_after_editing = {
        name: document.getElementById("attr_name").value + ';;' + document.getElementById("attr_name_english").value,
        x: attr_for_editing['x'],
        y: attr_for_editing['y'],
        description: document.getElementById("desc").value + ';;' + document.getElementById("desc_english").value,
        script: document.getElementById("subt").value + ';;' + document.getElementById("subt_english").value,
        picturesURLS: pixArr,
        videosURLS: vidArr
    };
    localStorage.setItem(attr_after_editing['name'] + "_vid", document.getElementById('nameOfVid').innerText);
    localStorage.setItem("desc_for_add_aq", attr_after_editing['description']);

    editRequestAttraction(attr_after_editing, attr_for_editing['id']);
    window.location.href = '/attractions';
}


function deletePoint() {
    getRequestAttractions(functionOfDelete);
}

function functionOfDelete(attractionsJSON) {

    let editedPoint = JSON.parse(localStorage.getItem("edited"));
    let lat = editedPoint.lat;
    let lng = editedPoint.lng;

    attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description: attr['description'], lat: attr['x'], lng: attr['y']};

        if ((p.lat).toFixed(8) == lat.toFixed(8) && (p.lng).toFixed(8) == lng.toFixed(8)) {
            deleteRequestAttractionSync(attr['id']);
            window.location.href = '/attractions';
        }
    });
}


function getFieldsValuesOfExistingAttraction(attractionsJSON) {
    let editedPoint = JSON.parse(localStorage.getItem("edited"));
    let lat = editedPoint.lat;
    let lng = editedPoint.lng;

    attractionsJSON.forEach(function (attr) {
        let p = {
            id: attr['id'],
            name: attr['name'],
            description: attr['description'],
            script: attr['script'],
            lat: attr['x'],
            lng: attr['y']
        };
        if (p.lat === lat && (p.lng).toFixed(8) === lng.toFixed(8)) {
            attr_for_editing = attr;
            initializeLanguageBTNs();
            let names = p.name.split(';;');
            let descriptions = p.description.split(';;');
            // let scripts = p.script.split(';;');
            document.getElementById("attr_name").value = names[0];
            document.getElementById("desc").value = descriptions[0];
            document.getElementById("attr_name_english").value = names[1];
            document.getElementById("desc_english").value = descriptions[1];
            //   document.getElementById("subt").value = scripts[0];
            // document.getElementById("subt_english").value = scripts[1];
            var video = document.getElementById('vid_itself');
            video.src = attr['videosURLS'];
            localStorage.setItem("name_for_add_aq", p.name);
            localStorage.setItem("desc_for_add_aq", p.description);
            document.getElementById('nameOfVid').innerText = localStorage.getItem("" + p.name + "_vid");
        }
    });
}


function initializeTheListOfPicturesToShow() {
    //Check File API support
    if (window.File && window.FileList && window.FileReader) {
        var filesInput = document.getElementById("files");

        filesInput.addEventListener("change", function (event) {

            var files = event.target.files; //FileList object
            var output = document.getElementById("result");

            for (var i = 0; i < files.length; i++) {
                var file = files[i];

                //Only pics
                if (!file.type.match('image'))
                    continue;

                var picReader = new FileReader();

                picReader.addEventListener("load", function (event) {

                    var picFile = event.target;

                    var div = document.createElement("div");

                    div.innerHTML = "<img class='thumbnail' src='" + picFile.result + "'" +
                        "title='" + picFile.name + "'/>";

                    let picURL = picFile.result;
                    arrOfPicsData.push(picURL);
                    output.insertBefore(div, null);

                });

                //Read the image
                picReader.readAsDataURL(file);
            }

        });
    } else {
        console.log("Your browser does not support File API");
    }
}

function initializeLanguageBTNs() {

    let attr_name = document.getElementById("attr_name");
    let attr_name_english = document.getElementById("attr_name_english");
    let subt = document.getElementById("subt");
    let subt_english = document.getElementById("subt_english");
    let desc = document.getElementById("desc");
    let desc_english = document.getElementById("desc_english");
    let hebrewBTN = document.getElementById("hebrewBTN");
    let englishBTN = document.getElementById("englishBTN");

    hebrewBTN.addEventListener('click', function () {
        attr_name.style.display = "";
        subt.style.display = "";
        attr_name_english.style.display = "none";
        subt_english.style.display = "none";
        desc.style.display = "";
        desc_english.style.display = "none";
    });

    englishBTN.addEventListener('click', function () {
        attr_name.style.display = "none";
        subt.style.display = "none";
        attr_name_english.style.display = "";
        subt_english.style.display = "";
        desc.style.display = "none";
        desc_english.style.display = "";
    });
}

function showVals() {
    getRequestAttractions(getName);
}

function editRequestAttraction(attraction, attr_id) {
    serverRequest("PUT", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/attraction/' + attr_id + '/',
        JSON.stringify(attraction));
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

function deleteRequestAttractionSync(id) {
    syncServerRequest("DELETE", function noop(dummy) {
    }, 'http://' + ip + ':12344/managementsystem/attraction/' + id + '/');
}