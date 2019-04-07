
window.onload = function() {
    let feedback_question = document.getElementById("fbquestion");
    let feedback_type = document.getElementById("feedback_type");
    let sendBTN = document.getElementById("send_feedback");
    sendBTN.addEventListener('click', function () {
        let feed_type;
        if(feedback_type.value == 'opt1')
            feed_type = 'FT';
        else
            feed_type = 'FR';

        let feed_to_send = {question:feedback_question.value , kind: feed_type};

        postRequestFeedback(feed_to_send);

    });

};


function postRequestFeedback(fb){
    //alert("aq blat");
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/feedback/',
        JSON.stringify(fb));
}