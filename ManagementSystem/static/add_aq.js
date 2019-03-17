function addAQ(){
    let ans1=document.getElementById("ans1").value;
    let ans2=document.getElementById("ans2").value;
    let ans3=document.getElementById("ans3").value;
    let ans4=document.getElementById("ans4").value;
    let answers = [ans1,ans2,ans3,ans4]; // might need to be a list(if theres a way) and not an array


    let american_question_to_send = {
            question :document.getElementById("ques").value
            ,answers: answers
            ,indexOfCorrectAnswer: Number(document.getElementById("correctAns").value),
            attraction:"" //atraction id needs to be here
    };
        // postRequestAQ(american_question_to_send);

        window.location.href='/add_hint';
}