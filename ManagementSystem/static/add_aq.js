
function postRequestAmericanQuestion(aq,attr_id){
    alert("aq blat");
    serverRequest("POST", function noop(dummy){}, 'http://10.0.0.7:12344/managementsystem/attraction/'+
        attr_id+'/aquestion/',
        JSON.stringify(aq));
}


function addAQ(){

    // let ans1=document.getElementById("ans1").value;
    // let ans2=document.getElementById("ans2").value;
    // let ans3=document.getElementById("ans3").value;
    // let ans4=document.getElementById("ans4").value;
    // let answers = [ans1,ans2,ans3,ans4]; // might need to be a list(if theres a way) and not an array
    //
    //
    // let american_question_to_send = {
    //         question :document.getElementById("ques").value
    //         ,answers: answers
    //         ,indexOfCorrectAnswer: Number(document.getElementById("correctAns").value),
    //         attraction:"" //atraction id needs to be here
    // };
        // postRequestAQ(american_question_to_send);
        getRequestAttractions(funcToGetAttraction);
        // postRequestAmericanQuestion(american_question_to_send);
        window.location.href='/add_hint';
}


    function funcToGetAttraction(attractionsJSON) {
alert("sada");

        let name = JSON.parse(localStorage.getItem("name_for_add_aq"));
        let desc = JSON.parse(localStorage.getItem("desc_for_add_aq"));
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
      attractionsJSON.forEach(function (attr) {
          // alert("the id is: "+attr['id']);
        let p = {name: attr['name'], description:attr['description']};
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if(p.name==name&&p.description==desc)
        {
            let ans1=document.getElementById("ans1").value;
            let ans2=document.getElementById("ans2").value;
            let ans3=document.getElementById("ans3").value;
            let ans4=document.getElementById("ans4").value;
            let answers = [ans1,ans2,ans3,ans4]; // might need to be a list(if theres a way) and not an array

alert("sada");

            let american_question_to_send = {
                    question :document.getElementById("ques").value
                    ,answers: answers
                    ,indexOfCorrectAnswer: Number(document.getElementById("correctAns").value)
                    ,attraction:attr['id'] //atraction id needs to be here
            };
alert("sada");
            postRequestAmericanQuestion(american_question_to_send,attr['id']);
        }
      });
        // alert("cant believe this is happenning!");
    }
