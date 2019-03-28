window.onload = function() {
    // alert("way");
    var addAqBTN = document.getElementById('finish_add_aq');
    addAqBTN.addEventListener('click', function() {
        getRequestAttractions(funcToGetAttraction);
        //alert("2");
        // window.location.href='/add_hint';
    });

}



function postRequestAmericanQuestion(aq,attr_id){
    alert("aq blat");
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+
        attr_id+'/aquestion/',
        JSON.stringify(aq));
}

 function funcToGetAttraction(attractionsJSON) {
        let name = localStorage.getItem("name_for_add_aq");
        let desc = localStorage.getItem("desc_for_add_aq");
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
        attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description:attr['description']};
       // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if(p.name===name && p.description===desc)
        {
            let ans1=document.getElementById("ans1").value;
            let ans2=document.getElementById("ans2").value;
            let ans3=document.getElementById("ans3").value;
            let ans4=document.getElementById("ans4").value;
            let answers = [ans1,ans2,ans3,ans4]; // might need to be a list(if theres a way) and not an array

            let american_question_to_send = {
                    question :document.getElementById("ques").value
                    ,answers: answers
                    ,indexOfCorrectAnswer: Number(document.getElementById("correctAns").value)
                    ,attraction:attr['id'] //atraction id needs to be here
            };
            postRequestAmericanQuestion(american_question_to_send,attr['id']);
            localStorage.setItem("the_attr", JSON.stringify(attr));
            window.location.href='/add_hint';
        }
      });
        // alert("cant believe this is happenning!");
    }



