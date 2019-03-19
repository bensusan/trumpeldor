var attractionObjToUseInHintEdit;

window.onload=function () {
    document.getElementById("hints_id_in_edit").innerHTML = localStorage.getItem("hint_id_to_edit");

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
                var hints_current_data = hint['data'];
                document.getElementById('write_hint_text_in_edit').value = hints_current_data;
                var finishEditionOfHintBTN = document.getElementById('submit_to_edit_hint');
                finishEditionOfHintBTN.addEventListener('click', function() {
                    let text_of_edition_in_hint = document.getElementById("write_hint_text_in_edit").value;
                    let hint_to_send = {
                        attraction: attractionObjToUseInHintEdit,
                        kind:'HT',
                        data:text_of_edition_in_hint
                    }
                    editRequestHint(hint_to_send,localStorage.getItem("attr_id_for_hint_edit"),localStorage.getItem("hint_id_to_edit"));
                    window.location.href='/pick_hints';
            });
            }
        });
}

function editRequestHint(the_hint,attr_id,hint_id){
    alert("edit hint huibla");
    serverRequest("PUT", function noop(dummy){}, 'http://10.0.0.7:12344/managementsystem/attraction/'+attr_id+'/hint/'+hint_id,
        JSON.stringify(the_hint));
}