var attractionObjToUseInHintEdit;

window.onload=function () {
    document.getElementById("hints_id_in_edit").innerHTML = localStorage.getItem("hint_id_to_edit");
    getRequestAttractions(funcForGettingCurrHintData);
};



function funcForGettingCurrHintData(attractionsJSON) {
    let name = localStorage.getItem("name_for_add_aq");
    let desc = localStorage.getItem("desc_for_add_aq");
    // alert("in get name! "+"of the origin : " + lat + " , " + lng);
    attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description: attr['description']};
        if (p.name === name && p.description === desc) {
            getRequestHints(hints_func_in_edit, attr['id']);
            attractionObjToUseInHintEdit = attr;
        }
    })
}

function hints_func_in_edit(hintsJSON) {
        hintsJSON.forEach(function (hint) {
            if(hint['id']==localStorage.getItem("hint_id_to_edit")){
                document.getElementById('write_hint_text_in_edit').value = hint['data'];
                let finishEditionOfHintBTN = document.getElementById('submit_to_edit_hint');
                finishEditionOfHintBTN.addEventListener('click', function() {
                   // alert(document.getElementById("write_hint_text_in_edit").value);
                    let hint_to_send = {
                        attraction: attractionObjToUseInHintEdit,
                        kind:'HT',
                        data:document.getElementById("write_hint_text_in_edit").value
                    };
                    editRequestHint(hint_to_send,localStorage.getItem("attr_id_for_hint_edit"),localStorage.getItem("hint_id_to_edit"));
                     window.location.href='/pick_hint_edit';
            });
            }
        });
}

function editRequestHint(the_hint,attr_id,hint_id){
  //  alert("edit hint huibla");
    serverRequest("PUT", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+attr_id+'/hint/'+hint_id+'/',
        JSON.stringify(the_hint));
}