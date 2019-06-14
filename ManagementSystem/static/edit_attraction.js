var attr_for_editing;
var helperVar;
var helperVarVid;


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
    let saveEditBTN = document.getElementById("saveEditBTN");
    saveEditBTN.addEventListener('click',function () {
        finishEditingAttraction();
    });
    let deletePointBTN = document.getElementById("delete_point");
    deletePointBTN.addEventListener('click',function () {
        deletePoint();
    });
    getRequestAttractions(getFieldsValuesOfExistingAttraction);
    localFileVideoPlayer();
};


function uploadVideoBTNclick() {
    let vid_input = document.getElementById('video_input');
    vid_input.click();
}


function finishEditingAttraction() {
    let attr_after_editing;
    let vidArr = attr_for_editing['videosURLS'];
    if (helperVarVid != undefined) {
        vidArr = [];
        vidArr.push(helperVarVid);
    }

    if (helperVar == undefined) {
        attr_after_editing = {
            name: document.getElementById("attr_name").value + ';;' + document.getElementById("attr_name_english").value,
            x: attr_for_editing['x'],
            y: attr_for_editing['y'],
            description: document.getElementById("desc").value + ';;' + document.getElementById("desc_english").value,
            picturesURLS: attr_for_editing['picturesURLS'],
            videosURLS: vidArr
        };
    } else {
        let picArr = [];
        picArr.push(helperVar);
        attr_after_editing = {
            name: document.getElementById("attr_name").value + ';;' + document.getElementById("attr_name_english").value,
            x: attr_for_editing['x'],
            y: attr_for_editing['y'],
            description: document.getElementById("desc").value + ';;' + document.getElementById("desc_english").value,
            picturesURLS: picArr,
            videosURLS: vidArr
        };
    }
    if (helperVarVid != undefined) {
        vidArr = [];
        vidArr.push(helperVarVid);
        //localStorage.clear();
        localStorage.setItem(attr_after_editing['name']+"_vid",vidArr);
    }
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
            deleteRequestAttraction(attr['id']);
            window.location.href = '/attractions';
        }
    });
}


function getFieldsValuesOfExistingAttraction(attractionsJSON) {
    let editedPoint = JSON.parse(localStorage.getItem("edited"));
    let lat = editedPoint.lat;
    let lng = editedPoint.lng;

    attractionsJSON.forEach(function (attr) {
        // alert("the id is: "+attr['id']);
        let p = {id: attr['id'], name: attr['name'], description: attr['description'], lat: attr['x'], lng: attr['y']};
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if (p.lat === lat && (p.lng).toFixed(8) === lng.toFixed(8)) {
            //  let picsRetreive = attr['picturesURLS'];
            attr_for_editing = attr;
            // name=p.name;

            initializeLanguageBTNs();
            let names = p.name.split(';;');
            let descriptions = p.description.split(';;');
            document.getElementById("attr_name").value = names[0];
            document.getElementById("desc").value = descriptions[0];
            document.getElementById("attr_name_english").value = names[1];
            document.getElementById("desc_english").value = descriptions[1];
            // var image = document.getElementById('output');
            // image.src = attr['picturesURLS'][0];
            // alert(JSON.parse(localStorage.getItem(p.name+"_pics")));
            initializeTheListOfPicturesToShow(JSON.parse(localStorage.getItem(p.name+"_pics")));
            var video = document.getElementById('vid_itself');
            video.src = localStorage.getItem(p.name+"_vid");
            localStorage.setItem("name_for_add_aq", p.name);
            localStorage.setItem("desc_for_add_aq", p.description);
        }
    });
}

function initializeTheListOfPicturesToShow(arrOfPics) {

    //var files = event.target.files; //FileList object
    var files = arrOfPics;
    var output = document.getElementById("result");

    for (var i = 0; i < files.length; i++) {
        var file = files[i];
        var img = document.createElement("img");
        img.src = file;
        img.className = 'thumbnail';
        var div = document.createElement("div");
        div.appendChild(img);

        output.insertBefore(div, null);
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


function encodeVideoFileAsURL(element) {

    helperVarVid = "";

    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        //alert(reader.result)
        helperVarVid = reader.result
    };

    reader.readAsDataURL(file);
}