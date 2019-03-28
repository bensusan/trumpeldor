var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};

var str;
var attractionObjToUseInHintDelete;

function funcForExistingAmericanQuestions(attractionsJSON){
        let name = localStorage.getItem("name_for_add_aq");
        let desc = localStorage.getItem("desc_for_add_aq");
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
        attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description:attr['description']};
        if(p.name===name && p.description===desc)
        {
            getRequestAmericanQuestions(AmericanQuestions_func,attr['id']);
            attractionObjToUseInHintDelete=attr;
        }
        });

}

function AmericanQuestions_func(AmericanQuestionsJSON) {
        str="";
        AmericanQuestionsJSON.forEach(function (aq) {
            str=str+"id: "+aq['id'] +", question: "+ aq['question']+", answers: "+ aq['answers']+", indexOfCorrectAnswer: "+ aq['indexOfCorrectAnswer']+"<br />";
            // alert(str);
        });
        document.getElementById("existing_aqs").innerHTML = str ;
}

window.onload = function () {
    getRequestAttractions(funcForExistingAmericanQuestions);
//////////////////////////////////////////////////////////////////////////////////////////
    var shiri = document.getElementById('shirimaimon');
        shiri.addEventListener('click', function() {
            alert("Shiri Maimon Kusit!");
        });
/////////////////////////////////////////////////////////////////////////////////////////////////////

    var wantToEditBTN = document.getElementById('want_to_edit_aq');
        wantToEditBTN.addEventListener('click', function() {
            var writeChosenHintTextEdit = document.getElementById("write_aq_id_to_edit");
            writeChosenHintTextEdit.style.display = "inline";

            var editChosenHintBTN = document.getElementById("edit_chosen_aq");
            editChosenHintBTN.style.display = "inline";

            editChosenHintBTN.addEventListener('click', function() {
                let hint_id_that_was_picked = document.getElementById("write_aq_id_to_edit").value;
                localStorage.setItem("aq_id_to_edit", hint_id_that_was_picked);
                localStorage.setItem("attr_id_for_aq_edit", attractionObjToUseInHintDelete['id']);
                window.location.href='/edit_hint';
            });
        });

    var wantToDeleteBTN = document.getElementById('want_to_delete_aq');
        wantToDeleteBTN.addEventListener('click', function() {
            var writeChosenHintText = document.getElementById("write_aq_id_to_delete");
            writeChosenHintText.style.display = "inline";

            var deleteChosenHintBTN = document.getElementById("delete_chosen_aq");
            deleteChosenHintBTN.style.display = "inline";

            deleteChosenHintBTN.addEventListener('click', function() {
                getRequestAmericanQuestions(funcInOrderToDeleteAmericanQuestion,attractionObjToUseInHintDelete['id']);
            });
        });


        localFileVideoPlayer();

};


function funcInOrderToDeleteAmericanQuestion(AmericanQuestionsJSON) {
    let aq_id_that_was_picked = document.getElementById("write_aq_id_to_delete").value;
   // let number_hint_id = Number(hint_id_that_was_picked);
      AmericanQuestionsJSON.forEach(function (aq) {
          // alert("the id is: "+attr['id']);
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if(aq['id']==aq_id_that_was_picked)
        {
            //alert("before delete aq!");
            deleteRequestAmericanQuestion(attractionObjToUseInHintDelete['id'],aq['id']);
            window.location.href='/pick_aq';
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



function donePickingAqs() {
    window.location.href='/attractions';
}


function getRequestAmericanQuestions(funcOnAqs,attr_id){
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    serverRequest("GET", funcOnAqs, 'http://'+ip+':12344/managementsystem/attraction/'+ attr_id+
        '/aquestion/?format=json');
    //alert("need to remove this alert and fix funcToGetAttraction()!");
}


function postRequestAmericanQuestion(aq,attr_id){
  //  alert("aq blat");
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+
        attr_id+'/aquestion/',
        JSON.stringify(aq));
}

function deleteRequestAmericanQuestion(attr_id,aq_id){
     serverRequest("DELETE", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+attr_id+'/aquestion/'+aq_id+'/');
    }