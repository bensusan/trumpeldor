let aq_id_that_was_picked_del;
let aq_id_that_was_picked_edit;
let aq_arr_for_test = [];
var str;
var attractionObjToUseInHintDelete;

window.onload = function () {
    getRequestAttractions(funcForExistingAmericanQuestions);

    initBtns();
        localFileVideoPlayer();

};


function initBtns() {
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
                let opts = document.getElementById('edit_cb');
                aq_id_that_was_picked_edit = opts.options[opts.selectedIndex].value;
                localStorage.setItem("aq_id_to_edit", aq_id_that_was_picked_edit);
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
}

function funcForExistingAmericanQuestions(attractionsJSON){
        let name = localStorage.getItem("name_for_add_aq");
        let desc = localStorage.getItem("desc_for_add_aq");
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
        attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description:attr['description']};
        if(p.name===name && p.description===desc)
        {
            getRequestAmericanQuestions(showInnerHtmlAndLoadValuesToComboBox,attr['id']);
            attractionObjToUseInHintDelete=attr;
        }
        });

}


function showInnerHtmlAndLoadValuesToComboBox(AmericanQuestionsJSON) {
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
            let ansString = "";
            aq['answers'].forEach(function (ans) {
                ansString += "&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"+ans+"</br>";
            });
            str=str+"<pre>"+aq['id']+".</br>" +"question:"+ aq['question']+"</br>answers: </br>"+ ansString+"indexOfCorrectAnswer: "+ aq['indexOfCorrectAnswer']+"</pre>";
            // alert(str);
            aq_arr_for_test.push(aq);
        });
        document.getElementById("existing_aqs").innerHTML = str ;
}


function funcInOrderToDeleteAmericanQuestion(AmericanQuestionsJSON) {
    var comboDelete = document.getElementById("delete_cb");
    aq_id_that_was_picked_del = comboDelete.options[comboDelete.selectedIndex].value;
   // let number_hint_id = Number(hint_id_that_was_picked);
      AmericanQuestionsJSON.forEach(function (aq) {
        if(aq['id']==aq_id_that_was_picked_del)
        {
            deleteRequestAmericanQuestion(attractionObjToUseInHintDelete['id'],aq['id']);
            window.location.href='/pick_aq_edit';
        }
      });

}


function donePickingAqs() {
    window.location.href='/edit_attraction';
}


function getRequestAmericanQuestions(funcOnAqs,attr_id){
    serverRequest("GET", funcOnAqs, 'http://'+ip+':12344/managementsystem/attraction/'+ attr_id+
        '/aquestion/?format=json');
}


function deleteRequestAmericanQuestion(attr_id,aq_id){
     serverRequest("DELETE", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+attr_id+'/aquestion/'+aq_id+'/');
    }