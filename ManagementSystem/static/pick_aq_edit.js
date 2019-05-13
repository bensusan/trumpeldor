
let aq_arr_for_test = [];
let id_to_delete=100;

window.onload = function () {
    getRequestAttractions(funcForExistingAmericanQuestions);

    var wantToEditBTN = document.getElementById('want_to_edit_aq');
    // var writeChosenHintTextEdit = document.getElementById("write_aq_id_to_edit");
    var editChosenHintBTN = document.getElementById("edit_chosen_aq");
    var wantToDeleteBTN = document.getElementById('want_to_delete_aq');
    // var writeChosenHintText = document.getElementById("write_aq_id_to_delete");
    var deleteChosenHintBTN = document.getElementById("delete_chosen_aq");
    var comboEdit = document.getElementById("edit_cb");
    var delTitle = document.getElementById("deleteTitle");
    var edTitle = document.getElementById("editTitle");
    var comboDelete = document.getElementById("delete_cb");

        wantToEditBTN.addEventListener('click', function() {
            comboEdit.style.display = "inline";
            edTitle.style.display = "inline";
            editChosenHintBTN.style.display = "inline";
            comboDelete.style.display = "none";
            delTitle.style.display = "none";
            deleteChosenHintBTN.style.display = "none";


            editChosenHintBTN.addEventListener('click', function() {
                let hint_id_that_was_picked = document.getElementById("write_aq_id_to_edit").value;
                localStorage.setItem("aq_id_to_edit", hint_id_that_was_picked);
                localStorage.setItem("attr_id_for_aq_edit", attractionObjToUseInHintDelete['id']);
                window.location.href='/edit_aq';
            });
        });

        wantToDeleteBTN.addEventListener('click', function() {
            comboDelete.style.display = "inline";
            delTitle.style.display = "inline";
            deleteChosenHintBTN.style.display = "inline";
            editChosenHintBTN.style.display = "none";
            comboEdit.style.display = "none";
            edTitle.style.display = "none";

            deleteChosenHintBTN.addEventListener('click', function() {
                getRequestAmericanQuestions(funcInOrderToDeleteAmericanQuestion,attractionObjToUseInHintDelete['id']);
            });
        });
        localFileVideoPlayer();

};


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
        let i=1;
        AmericanQuestionsJSON.forEach(function (aq) {
            let e_opt_id = "ecb"+i;
            let d_opt_id = "dcb"+i;

            document.getElementById(e_opt_id).innerText = aq['id'];
            document.getElementById(e_opt_id).value = aq['id'];
            document.getElementById(e_opt_id).style.display='inline';

            document.getElementById(d_opt_id).innerText = aq['id'];
            document.getElementById(d_opt_id).value = aq['id'];
            document.getElementById(d_opt_id).style.display='inline';
            i=i+1;
            str=str+"id: "+aq['id'] +", question: "+ aq['question']+", answers: "+ aq['answers']+", indexOfCorrectAnswer: "+ aq['indexOfCorrectAnswer']+"<br />";
            // alert(str);
            aq_arr_for_test.push(aq);
        });
        document.getElementById("existing_aqs").innerHTML = str ;
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





function donePickingAqs() {
    window.location.href='/edit_attraction';
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