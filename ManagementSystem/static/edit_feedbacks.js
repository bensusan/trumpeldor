
let aq_arr_for_test = [];
let id_to_delete=100;

window.onload = function () {
    getRequestFeedbacks(funcForExistingFeedbacks);
    var wantToEditBTN = document.getElementById('want_to_edit_aq');
    var writeChosenHintTextEdit = document.getElementById("write_aq_id_to_edit");
    var editChosenHintBTN = document.getElementById("edit_chosen_aq");
    var wantToDeleteBTN = document.getElementById('want_to_delete_aq');
    var writeChosenHintText = document.getElementById("write_aq_id_to_delete");
    var deleteChosenHintBTN = document.getElementById("delete_chosen_aq");

        wantToEditBTN.addEventListener('click', function() {
            writeChosenHintTextEdit.style.display = "inline";
            editChosenHintBTN.style.display = "inline";
             writeChosenHintText.style.display = "none";
            deleteChosenHintBTN.style.display = "none";
            editChosenHintBTN.addEventListener('click', function() {
                let hint_id_that_was_picked = document.getElementById("write_aq_id_to_edit").value;
                localStorage.setItem("aq_id_to_edit", hint_id_that_was_picked);
                localStorage.setItem("attr_id_for_aq_edit", attractionObjToUseInHintDelete['id']);
                window.location.href='/edit_aq';
            });
        });

        wantToDeleteBTN.addEventListener('click', function() {
            writeChosenHintText.style.display = "inline";
            deleteChosenHintBTN.style.display = "inline";
            writeChosenHintTextEdit.style.display = "none";
            editChosenHintBTN.style.display = "none";
            deleteChosenHintBTN.addEventListener('click', function() {
                getRequestAmericanQuestions(funcInOrderToDeleteAmericanQuestion,attractionObjToUseInHintDelete['id']);
            });
        });

};


function wantToChangeButton(){
        var change_txt = document.getElementById("write_fb_to_change");
            change_txt.style.display = "inline";

            var change_btn = document.getElementById("edit_chosen_fb");
            change_btn.style.display = "inline";

            var delete_txt = document.getElementById("write_fb_id_to_delete");
            delete_txt.style.display = "none";

            var delete_btn = document.getElementById("delete_chosen_fb");
            delete_btn.style.display = "none";

            change_btn.addEventListener('click', function() {
                change_txt.style.display = "none";
                change_btn.style.display = "none";


            });
}


function wantToDeleteButton(){
        var change_txt = document.getElementById("write_fb_to_change");
            change_txt.style.display = "none";

            var change_btn = document.getElementById("edit_chosen_fb");
            change_btn.style.display = "none";

            var delete_txt = document.getElementById("write_fb_id_to_delete");
            delete_txt.style.display = "inline";

            var delete_btn = document.getElementById("delete_chosen_fb");
            delete_btn.style.display = "inline";

            delete_btn.addEventListener('click', function() {
                let fb_id = delete_txt.value;
                deleteRequestFeedback(fb_id);
                window.location.href='/edit_feedbacks';

            });
}

var str;
var attractionObjToUseInHintDelete;

function funcForExistingFeedbacks(feedbacksJSON){
        str="";
        feedbacksJSON.forEach(function (fb) {
        str=str+"id: "+fb['id']+", question: "+fb['question']+", Type: "+fb['kind']+"<br />";
        });
        document.getElementById("existing_fbs").innerHTML = str ;

}



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
            window.location.href='/pick_aq_edit';
        }
      });

}


function doneEditingFbs() {
    window.location.href='/main';
}


function getRequestFeedbacks(funcOnAqs){
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    serverRequest("GET", funcOnAqs, 'http://'+ip+':12344/managementsystem/feedback/?format=json');
    //alert("need to remove this alert and fix funcToGetAttraction()!");
}


function postRequestAmericanQuestion(aq,attr_id){
  //  alert("aq blat");
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+
        attr_id+'/aquestion/',
        JSON.stringify(aq));
}

function deleteRequestFeedback(fb_id){
     serverRequest("DELETE", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/feedback/'+fb_id+'/');
    }