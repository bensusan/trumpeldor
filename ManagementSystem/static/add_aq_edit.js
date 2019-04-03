
const Http = new XMLHttpRequest();
let loop_add_aq = true;

window.onload = function() {
    let noOfAns = document.getElementById('noOfAns');
    let noOfCorrect = document.getElementById('noOfCorrect');
    let okBTN = document.getElementById('ok_button_to_prepare');
    let addAqBTN = document.getElementById('finish_add_aq_btn');
    let txt1 = document.getElementById('txt1');
    let txt2 = document.getElementById('txt2');

    let ques = document.getElementById('ques');
    let ans1 = document.getElementById('ans1');
    let ans2 = document.getElementById('ans2');
    let ans3 = document.getElementById('ans3');
    let ans4 = document.getElementById('ans4');
    let ans5 = document.getElementById('ans5');
    let ans6 = document.getElementById('ans6');
    let ans7 = document.getElementById('ans7');
    let ans8 = document.getElementById('ans8');
    let correctAns = document.getElementById('correctAns');
    let correctAns2 = document.getElementById('correctAns2');
    let correctAns3 = document.getElementById('correctAns3');

    okBTN.addEventListener('click',function () {
    alert("sad");
    let numberOfAns = noOfAns.value;
    let numberOfCorrectAns = noOfCorrect.value;

    okBTN.style.display = "none";
    txt1.style.display = "none";
    txt2.style.display = "none";
    noOfAns.style.display = "none";
    noOfCorrect.style.display = "none";
    addAqBTN.style.display = "inline";
    ques.style.display = "inline";
    ans1.style.display = "inline";
    ans2.style.display = "inline";
    ans3.style.display = "inline";
    correctAns.style.display = "inline";

    if(numberOfAns == "4")
    {
    ans4.style.display = "inline";
    }
    if(numberOfAns == "5")
    {
    ans4.style.display = "inline";
    ans5.style.display = "inline";
    }
    if(numberOfAns == "6")
    {
    ans4.style.display = "inline";
    ans5.style.display = "inline";
    ans6.style.display = "inline";
    }
    if(numberOfAns == "7")
    {
    ans4.style.display = "inline";
    ans5.style.display = "inline";
    ans6.style.display = "inline";
    ans7.style.display = "inline";
    }
    if(numberOfAns == "8")
    {
    ans4.style.display = "inline";
    ans5.style.display = "inline";
    ans6.style.display = "inline";
    ans7.style.display = "inline";
    ans8.style.display = "inline";
    }

    if(numberOfCorrectAns == "2")
    {
    correctAns2.style.display = "inline";
    }
    if(numberOfCorrectAns == "3")
    {
    correctAns2.style.display = "inline";
    correctAns3.style.display = "inline";
    }
    });

    addAqBTN.addEventListener('click', function() {
        getRequestAttractionsi(funcToGetAttraction);
        //alert("2");
        //setTimeout(finishAddAq ,10);
    });

};

function serverRequestInAddAq(getOrPost, functionOnReady, url, post=null){
    Http.onreadystatechange = function(){
        if(Http.readyState === 4 && Http.status === 200){
            functionOnReady(JSON.parse(Http.responseText));
        }
    };
    Http.open(getOrPost, url, true);
    if(post) {
        Http.setRequestHeader('Content-type','application/json; charset=utf-8');
        Http.send(post);
        window.location.href = '/pick_aq_edit';
        return false;
    }
    Http.send();
}

function getRequestAttractionsi(funcOnAttractions){
    // the server port and my ip
    serverRequestInAddAq("GET", funcOnAttractions, 'http://'+ip+':12344/managementsystem/attraction/?format=json');
    //alert("need to remove this alert and fix funcToGetAttraction()!");
}






function postRequestAmericanQuestion(aq,attr_id){
    //alert("aq blat");
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+
        attr_id+'/aquestion/',
        JSON.stringify(aq));
    //window.location.href='/pick_aq_edit';
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

            loop_add_aq=false;
        }
      });

loop_add_aq=false;
    }



