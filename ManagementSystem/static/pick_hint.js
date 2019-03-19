var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};

var str;
var attractionObjToUseInHintDelete;

function funcForExistingHints(attractionsJSON){
        let name = localStorage.getItem("name_for_add_aq");
        let desc = localStorage.getItem("desc_for_add_aq");
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
        attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description:attr['description']};
        if(p.name===name && p.description===desc)
        {
            getRequestHints(hints_func,attr['id']);
            attractionObjToUseInHintDelete=attr;
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

window.onload = function () {
    getRequestAttractions(funcForExistingHints);

    var wantToEditBTN = document.getElementById('want_to_edit_hint');
        wantToEditBTN.addEventListener('click', function() {
            var writeChosenHintTextEdit = document.getElementById("write_hint_id_to_edit");
            writeChosenHintTextEdit.style.display = "inline";

            var editChosenHintBTN = document.getElementById("edit_chosen_hint");
            editChosenHintBTN.style.display = "inline";

            editChosenHintBTN.addEventListener('click', function() {
                let hint_id_that_was_picked = document.getElementById("write_hint_id_to_edit").value;
                localStorage.setItem("hint_id_to_edit", hint_id_that_was_picked);
                localStorage.setItem("attr_id_for_hint_edit", attractionObjToUseInHintDelete['id']);
                window.location.href='/edit_hint';
            });
        });

    var wantToDeleteBTN = document.getElementById('want_to_delete_hint');
        wantToDeleteBTN.addEventListener('click', function() {
            var writeChosenHintText = document.getElementById("write_hint_id_to_delete");
            writeChosenHintText.style.display = "inline";

            var deleteChosenHintBTN = document.getElementById("delete_chosen_hint");
            deleteChosenHintBTN.style.display = "inline";

            deleteChosenHintBTN.addEventListener('click', function() {
                getRequestHints(funcInOrderToDeleteHint,attractionObjToUseInHintDelete['id']);
            });
        });


        localFileVideoPlayer();

};

function funcInOrderToDeleteHint(hintsJSON) {
    let hint_id_that_was_picked = document.getElementById("write_hint_id_to_delete").value;
   // let number_hint_id = Number(hint_id_that_was_picked);
      hintsJSON.forEach(function (hint) {
          // alert("the id is: "+attr['id']);
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if(hint['id']==hint_id_that_was_picked)
        {
            alert("before delete hint!");
            deleteRequestHint(attractionObjToUseInHintDelete['id'],hint['id']);
            window.location.href='/pick_hint';
        }
      });

}

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

    function getTheAttr(attractionsJSON) {

        let editedPoint = JSON.parse(localStorage.getItem("edited"));
      let lat = editedPoint.lat;
      let lng = editedPoint.lng;
      //let name = "didn't found!!!";
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
      attractionsJSON.forEach(function (attr) {
          // alert("the id is: "+attr['id']);
        let p = {name: attr['name'], description:attr['description'], lat: attr['x'], lng: attr['y']};
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if(p.lat===lat&&(p.lng).toFixed(8)===lng.toFixed(8))
        {
            alert("before delete hint!");
            deleteRequestHint(attr['id'],);
            window.location.href='/pick_hint';
        }
      });
        // alert("cant believe this is happenning!");
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
    window.location.href='/attractions';
}


function getRequestHints(funcOnHints,attr_id){
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    serverRequest("GET", funcOnHints, 'http://10.0.0.7:12344/managementsystem/attraction/'+ attr_id+
        '/hint/?format=json');
    //alert("need to remove this alert and fix funcToGetAttraction()!");
}


function postRequestHint(the_hint,attr_id){
    alert("hint blat");
    serverRequest("POST", function noop(dummy){}, 'http://10.0.0.7:12344/managementsystem/attraction/'+
        attr_id+'/hint/',
        JSON.stringify(the_hint));
}

function deleteRequestHint(attr_id,hint_id){
     serverRequest("DELETE", function noop(dummy){}, 'http://10.0.0.7:12344/managementsystem/attraction/'+attr_id+'/hint/'+hint_id+'/');
    }