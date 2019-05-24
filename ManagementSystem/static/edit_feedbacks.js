
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

            var deletedFeedback = document.getElementById("write_fb_id_to_delete");
            deletedFeedback.style.display = "none";

            var delete_btn = document.getElementById("delete_chosen_fb");
            delete_btn.style.display = "none";

            change_btn.addEventListener('click', function() {
                let fb_id = change_txt.value;
                change_txt.style.display = "none";
                change_btn.style.display = "none";
                var firstTitle = document.getElementById("first");
                firstTitle.style.display = "inline";
                var feedback_question = document.getElementById("fbquestion");
                feedback_question.style.display = "inline";
                var secondTitle = document.getElementById("second");
                secondTitle.style.display = "inline";
                var feedback_type = document.getElementById("feedback_type");
                feedback_type.style.display = "inline";
                var sendFbBTN = document.getElementById("send_feedback");
                sendFbBTN.style.display = "inline";
                sendFbBTN.addEventListener('click', function() {
                    let feed_type;
                    if(feedback_type.value == 'opt1')
                        feed_type = "FT";
                    else
                        feed_type = "FR";

                    let feed_to_send = {question:feedback_question.value , kind: feed_type};

                    editRequestFeedback(feed_to_send,fb_id);
                    window.location.href='/edit_feedbacks';
                });

            });
}


function wantToDeleteButton(){
        var change_txt = document.getElementById("write_fb_to_change");
            change_txt.style.display = "none";

            var change_btn = document.getElementById("edit_chosen_fb");
            change_btn.style.display = "none";

            var deletedFeedback = document.getElementById("write_fb_id_to_delete");
            deletedFeedback.style.display = "inline";

            var delete_btn = document.getElementById("delete_chosen_fb");
            delete_btn.style.display = "inline";

            delete_btn.addEventListener('click', function() {
                let fb_id = deletedFeedback.options[deletedFeedback.selectedIndex].value;
                deleteRequestFeedback(fb_id);
                window.location.href='/edit_feedbacks';

            });
}

var str;
var attractionObjToUseInHintDelete;

function funcForExistingFeedbacks(feedbacksJSON){
        str="";
        let i=1;
        feedbacksJSON.forEach(function (fb) {
        let d_opt_id = "dcb"+i;
        document.getElementById(d_opt_id).innerText = fb['question']
            document.getElementById(d_opt_id).value = fb['id'];
        document.getElementById(d_opt_id).style.display='inline';
        i=i+1;
        str=str+"id: "+fb['id']+", question: "+fb['question']+", Type: "+fb['kind']+"<br />";
        });
        document.getElementById("existing_fbs").innerHTML = str ;
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


function deleteRequestFeedback(fb_id){
     serverRequest("DELETE", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/feedback/'+fb_id+'/');
    }

function editRequestFeedback(feedback,feedback_id){
   // alert("edit blat hui");
    serverRequest("PUT", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/feedback/'+feedback_id+'/',
        JSON.stringify(feedback));
}