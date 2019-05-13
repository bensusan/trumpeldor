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
        let i=1;
        hintsJSON.forEach(function (hint) {
            let e_opt_id = "ecb"+i;
            let d_opt_id = "dcb"+i;

            document.getElementById(e_opt_id).innerText = hint['data'];
            document.getElementById(e_opt_id).value = hint['id'];
            document.getElementById(e_opt_id).style.display='inline';

            document.getElementById(d_opt_id).innerText = hint['data'];
            document.getElementById(d_opt_id).value = hint['id'];
            document.getElementById(d_opt_id).style.display='inline';
            i=i+1;
            str=str+" data: "+ hint['data']+"<br />";
            // alert(str);
        });
        document.getElementById("existing_hints").innerHTML = str ;
        document.getElementById("existing_hints").style.fontWeight = 'bold';
        document.getElementById("existing_hints").style.fontFamily='david';
        document.getElementById("existing_hints").style.fontSize='24px';
}

window.onload = function () {
    getRequestAttractions(funcForExistingHints);
    localFileVideoPlayer();

};

function wantToEditButton(){
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

            editChosenHintBTN.addEventListener('click', function() {
                let chosen_hint_id = comboEdit.options[comboEdit.selectedIndex].value;
                // let hint_id_that_was_picked = document.getElementById("write_hint_id_to_edit").value;
                localStorage.setItem("hint_id_to_edit", chosen_hint_id);
                localStorage.setItem("attr_id_for_hint_edit", attractionObjToUseInHintDelete['id']);
                window.location.href='/edit_hint_edit';
            });
}


function wantToDeleteButton(){

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

            deleteChosenHintBTN.addEventListener('click', function() {
                getRequestHints(funcInOrderToDeleteHint,attractionObjToUseInHintDelete['id']);
            });
}

function funcInOrderToDeleteHint(hintsJSON) {
    var comboDelete = document.getElementById("delete_cb");
    let hint_id_that_was_picked = comboDelete.options[comboDelete.selectedIndex].value;
   // let number_hint_id = Number(hint_id_that_was_picked);
      hintsJSON.forEach(function (hint) {
          // alert("the id is: "+attr['id']);
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if(hint['id']==hint_id_that_was_picked)
        {
            //alert("before delete hint!");
            deleteRequestHint(attractionObjToUseInHintDelete['id'],hint['id']);
            window.location.href='/pick_hint_edit';
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
            window.location.href='/add_hint_edit';
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
            window.location.href='/pick_hint_edit';
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
    serverRequest("GET", funcOnHints, 'http://'+ip+':12344/managementsystem/attraction/'+ attr_id+
        '/hint/?format=json');
    //alert("need to remove this alert and fix funcToGetAttraction()!");
}


function postRequestHint(the_hint,attr_id){
 //   alert("hint blat");
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+
        attr_id+'/hint/',
        JSON.stringify(the_hint));
}

function deleteRequestHint(attr_id,hint_id){
     serverRequest("DELETE", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+attr_id+'/hint/'+hint_id+'/');
    }