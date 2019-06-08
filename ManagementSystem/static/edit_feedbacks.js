var str;
var attractionObjToUseInHintDelete;

window.onload = function () {
    getRequestFeedbacks(funcForExistingFeedbacks);
    initializeBtnsFunctionality();
};

function initializeBtnsFunctionality() {
    let editBTN = document.getElementById("edit_feedback");
    let deleteBTN = document.getElementById("delete_feedback");
    let editcb = document.getElementById("edit_cb");
    let deletecb = document.getElementById("delete_cb");
    let do_edit = document.getElementById("edit_chosen_fb");
    let do_delete = document.getElementById("delete_chosen_fb");
    let edit_txt = document.getElementById("fb_edit_txt");


    editBTN.addEventListener('click', function () {

        editcb.style.display = "";
        do_edit.style.display = "";
        edit_txt.style.display = "";
        deletecb.style.display = "none";
        do_delete.style.display = "none";
        do_edit.addEventListener('click', function () {
            let fb_id = editcb.options[editcb.selectedIndex].value;
            let type = localStorage.getItem("fbtype" + fb_id);
            let fb = {
                question:document.getElementById('fb_edit_txt').value,
                kind: type
            }
            editRequestFeedback(fb, fb_id);
            window.location.href = '/edit_feedbacks';
        });
    });

    deleteBTN.addEventListener('click', function () {
        editcb.style.display = "none";
        do_edit.style.display = "none";
        edit_txt.style.display = "none";
        deletecb.style.display = "";
        do_delete.style.display = "";
        do_delete.addEventListener('click', function () {
            let fb_id = deletecb.options[deletecb.selectedIndex].value;
            deleteRequestFeedback(fb_id);
            window.location.href = '/edit_feedbacks';
        });
    });
}

function funcForExistingFeedbacks(feedbacksJSON) {
    str = "";
    let i = 1;
    feedbacksJSON.forEach(function (fb) {
        let d_opt_id = "dcb" + i;
        let e_opt_id = "ecb" + i;
        localStorage.setItem("fbtype" + fb['id'], fb['kind']);
        document.getElementById(d_opt_id).innerText = fb['question']
        document.getElementById(d_opt_id).value = fb['id'];
        document.getElementById(d_opt_id).style.display = 'inline';
        document.getElementById(e_opt_id).innerText = fb['question']
        document.getElementById(e_opt_id).value = fb['id'];
        document.getElementById(e_opt_id).style.display = 'inline';
        i = i + 1;
        str = str + "id: " + fb['id'] + ", question: " + fb['question'] + ", Type: " + fb['kind'] + "<br />";
    });
    document.getElementById("existing_fbs").innerHTML = str;
}


function doneEditingFbs() {
    window.location.href = '/main';
}


function getRequestFeedbacks(funcOnAqs) {

    serverRequest("GET", funcOnAqs, 'http://' + ip + ':12344/managementsystem/feedback/?format=json');
}


function deleteRequestFeedback(fb_id) {
    serverRequest("DELETE", function noop(dummy) {
    }, 'http://' + ip + ':12344/managementsystem/feedback/' + fb_id + '/');
}

function editRequestFeedback(feedback, feedback_id) {
    serverRequest("PUT", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/feedback/' + feedback_id + '/',
        JSON.stringify(feedback));
}