var str;
var attractionObjToUseInHintDelete;

function funcForExistingHints(attractionsJSON) {
    let name = localStorage.getItem("name_for_add_aq");
    let desc = localStorage.getItem("desc_for_add_aq");
    // alert("in get name! "+"of the origin : " + lat + " , " + lng);
    attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description: attr['description']};
        if (p.name === name && p.description === desc) {
            getRequestHints(hints_func, attr['id']);
            attractionObjToUseInHintDelete = attr;
        }
    });

}


function hints_func(hintsJSON) {
    str = "";
    let imageCounter = 1;
    let videoCounter = 1;
    let i = 1;

    hintsJSON.forEach(function (hint) {
        let e_opt_id = "ecb" + i;
        let d_opt_id = "dcb" + i;
        document.getElementById(d_opt_id).innerText = hint['data'].split(';;')[0];
        document.getElementById(e_opt_id).innerText = hint['data'].split(';;')[0];

        document.getElementById(e_opt_id).value = hint['id'];
        document.getElementById(e_opt_id).style.display = '';
        document.getElementById(d_opt_id).value = hint['id'];
        document.getElementById(d_opt_id).style.display = '';
        i = i + 1;

        let dataOfHint = hint['data'];
        if (dataOfHint.substring(0, 16) == 'data:application')
            str = str + " data: " + "media" + imageCounter + "<br />";
        else {
            if (hint['data'].substring(0, 10) == 'data:video')
                str = str + " data: " + "VideoMedia" + videoCounter + "<br />";
            else
                str = str + (i-1) +". " + hint['data'].split(';;')[0] + "<br />";
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


function ffff(hintsJSON) {
    str = "";
    let i = 1;
    let imageCounter = 1;
    let videoCounter = 1;

    hintsJSON.forEach(function (hint) {
        let e_opt_id = "ecb" + i;
        let d_opt_id = "dcb" + i;

        if (hint['data'].substring(0, 16) == 'data:application') {
            document.getElementById(d_opt_id).innerText = "media" + imageCounter;
            document.getElementById(e_opt_id).innerText = "media" + imageCounter;
        } else {
            if (hint['data'].substring(0, 10) == 'data:video') {
                document.getElementById(d_opt_id).innerText = "VideoMedia" + videoCounter;
                document.getElementById(e_opt_id).innerText = "VideoMedia" + videoCounter;
            } else {
                document.getElementById(d_opt_id).innerText = hint['data'];
                document.getElementById(e_opt_id).innerText = hint['data'];
            }
        }

        document.getElementById(e_opt_id).value = hint['id'];
        document.getElementById(e_opt_id).style.display = '';
        document.getElementById(d_opt_id).value = hint['id'];
        document.getElementById(d_opt_id).style.display = '';
        i = i + 1;
        //data:application
        let dataOfHint = hint['data'];
        if (dataOfHint.substring(0, 16) == 'data:application')
            str = str + " data: " + "media" + imageCounter + "<br />";
        else {
            if (hint['data'].substring(0, 10) == 'data:video')
                str = str + " data: " + "VideoMedia" + videoCounter + "<br />";
            else
                str = str + hint['id'] + hint['data'].split(';;')[0] + "<br />";
        }

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

window.onload = function () {
    let editMenuBTN = document.getElementById('editHintBTNmenu');
    editMenuBTN.addEventListener('click', function () {
        wantToEditButton();
    });
    let deleteMenuBTN = document.getElementById('deleteHintBTNmenu');
    deleteMenuBTN.addEventListener('click', function () {
        wantToDeleteButton();
    });
    getRequestAttractions(funcForExistingHints);
    localFileVideoPlayer();

};


function wantToEditButton() {
    var delTitle = document.getElementById("deleteTitle");
    delTitle.style.display = "none";

    var deleteChosenHintBTN = document.getElementById("delete_chosen_hint");
    deleteChosenHintBTN.style.display = "none";

    var comboDelete = document.getElementById("delete_cb");
    comboDelete.style.display = "none";

    var edTitle = document.getElementById("editTitle");
    edTitle.style.display = "inline";

    var comboEdit = document.getElementById("edit_cb");
    comboEdit.style.display = "inline";

    var editChosenHintBTN = document.getElementById("edit_chosen_hint");
    editChosenHintBTN.style.display = "inline";

    window.scrollTo(0, document.body.scrollHeight);

    editChosenHintBTN.addEventListener('click', function () {
        let chosen_hint_id = comboEdit.options[comboEdit.selectedIndex].value;
        // let hint_id_that_was_picked = document.getElementById("write_hint_id_to_edit").value;
        localStorage.setItem("hint_id_to_edit", chosen_hint_id);
        localStorage.setItem("attr_id_for_hint_edit", attractionObjToUseInHintDelete['id']);
        window.location.href = '/edit_hint_edit';
    });
}


function wantToDeleteButton() {

    var editChosenHintBTN = document.getElementById("edit_chosen_hint");
    editChosenHintBTN.style.display = "none";

    var comboEdit = document.getElementById("edit_cb");
    comboEdit.style.display = "none";

    var delTitle = document.getElementById("deleteTitle");
    delTitle.style.display = "inline";

    var edTitle = document.getElementById("editTitle");
    edTitle.style.display = "none";

    var comboDelete = document.getElementById("delete_cb");
    comboDelete.style.display = "inline";

    var deleteChosenHintBTN = document.getElementById("delete_chosen_hint");
    deleteChosenHintBTN.style.display = "inline";

    window.scrollTo(0, document.body.scrollHeight);

    deleteChosenHintBTN.addEventListener('click', function () {
        getRequestHints(funcInOrderToDeleteHint, attractionObjToUseInHintDelete['id']);
    });
}

function funcInOrderToDeleteHint(hintsJSON) {
    var comboDelete = document.getElementById("delete_cb");
    let hint_id_that_was_picked = comboDelete.options[comboDelete.selectedIndex].value;
    // let number_hint_id = Number(hint_id_that_was_picked);
    hintsJSON.forEach(function (hint) {
        // alert("the id is: "+attr['id']);
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if (hint['id'] == hint_id_that_was_picked) {
            //alert("before delete hint!");
            deleteRequestHint(attractionObjToUseInHintDelete['id'], hint['id']);
            window.location.href = '/pick_hint_edit';
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


function donePickingHints() {
    window.location.href = '/attractions';
}


function getRequestHints(funcOnHints, attr_id) {
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    serverRequest("GET", funcOnHints, 'http://' + ip + ':12344/managementsystem/attraction/' + attr_id +
        '/hint/?format=json');
    //alert("need to remove this alert and fix funcToGetAttraction()!");
}


function postRequestHint(the_hint, attr_id) {
    //   alert("hint blat");
    serverRequest("POST", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/attraction/' +
        attr_id + '/hint/',
        JSON.stringify(the_hint));
}

function deleteRequestHint(attr_id, hint_id) {
    syncServerRequest("DELETE", function noop(dummy) {
    }, 'http://' + ip + ':12344/managementsystem/attraction/' + attr_id + '/hint/' + hint_id + '/');
}