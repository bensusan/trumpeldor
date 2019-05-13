var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};

var str;
var str2;
var attractionObjToUseInHintDelete;
let type = "sliding_puzzle";
let game_id_that_was_picked = 0;

function showingSelectOfType(){

    let game_type = document.getElementById("game_type");


    if(game_type.value == 'opt1')
                type = "puzzle";

    if(game_type.value == 'opt3')
                type = "";

    getRequestGames(showOpts,type,attractionObjToUseInHintDelete['id']);
}


function showOpts(gamesJSON) {

    let opts = document.getElementById("delete_cb");
    opts.style.display='';

    let i=1;
        gamesJSON.forEach(function (game) {
            let d_opt_id = "dcb"+i;

            document.getElementById(d_opt_id).innerText = game['description'];
            document.getElementById(d_opt_id).value = game['id'];
            document.getElementById(d_opt_id).style.display='';
            i=i+1;

        });

    var showChosenGameBTN = document.getElementById("show_chosen_game");
            showChosenGameBTN.style.display = '';

    showChosenGameBTN.addEventListener('click',function () {
         game_id_that_was_picked = opts.options[opts.selectedIndex].value;
         getRequestGames(doSome,type,attractionObjToUseInHintDelete['id']);
    });

    var deleteChosenHintBTN = document.getElementById("delete_chosen_hint");
            deleteChosenHintBTN.style.display = "";

    deleteChosenHintBTN.addEventListener('click', function() {
        deleteRequestGame(attractionObjToUseInHintDelete['id'],type);
        window.location.href = '/pick_delete_game';
    });


}

function doSome(gamesJSON){
    let namepic = "";

    if(type == "sliding_puzzle")
    { namepic = "piecesURLS"; }
    else
    { namepic = "pictureURL"; }

    gamesJSON.forEach(function (game) {
        if(game['id'] == game_id_that_was_picked)
        {
            var image = document.getElementById('output');
            image.src = game[namepic];
        }
    });
}

function funcForExistingHints(attractionsJSON){

        let name = localStorage.getItem("name_for_add_aq");
        let desc = localStorage.getItem("desc_for_add_aq");
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
        attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description:attr['description']};
        if(p.name===name && p.description===desc)
        {
            getRequestGames(games_func_sliding,"sliding_puzzle",attr['id']);
            // getRequestGames(games_func_drag,"puzzle",attr['id']);
            attractionObjToUseInHintDelete=attr;
        }
        });

}

function games_func_sliding(gamesJSON) {
        str="Sliding:<br />";
        gamesJSON.forEach(function (game) {
            str=str+"id: "+game['id'] +", instructions: "+ game['description']+"<br />";
            // alert(str);
        });
        // document.getElementById("existing_hints").innerHTML = str;
        // document.getElementById("existing_hints").style.fontWeight = 'bold';
        // document.getElementById("existing_hints").style.fontFamily='david';
        // document.getElementById("existing_hints").style.fontSize='24px';
}

function games_func_drag(gamesJSON) {
        str2="Drag:<br />";
        gamesJSON.forEach(function (game) {
            str2=str2+"id: "+game['id'] +", instructions: "+ game['description']+"<br />";
            // alert(str);
        });
        // document.getElementById("existing_hints_drag").innerHTML = str2;
        // document.getElementById("existing_hints_drag").style.fontWeight = 'bold';
        // document.getElementById("existing_hints_drag").style.fontFamily='david';
        // document.getElementById("existing_hints_drag").style.fontSize='24px';
}

window.onload = function () {
    let cb = document.getElementById("delete_cb");
    cb.onchange = function(){
        showingSelectOfType();
    };
    getRequestAttractions(funcForExistingHints);
    localFileVideoPlayer();

};

function wantToDeleteButton(){
        var writeChosenHintText = document.getElementById("write_hint_id_to_delete");
            writeChosenHintText.style.display = "inline";

            var titletype = document.getElementById("title_type");
            titletype.style.display = "inline";

            var game_type = document.getElementById("game_type");
            game_type.style.display = "inline";

            let type = "sliding_puzzle";


         var showChosenHintBTN = document.getElementById("show_chosen_game");
            showChosenHintBTN.style.display = "inline";

            var deleteChosenHintBTN = document.getElementById("delete_chosen_hint");
            deleteChosenHintBTN.style.display = "inline";

            showChosenHintBTN.addEventListener('click', function() {

            if(game_type.value == 'opt1')
                type = "puzzle";

            if(game_type.value == 'opt3')
                type = "";

            getRequestGames(func_to_show,type,attractionObjToUseInHintDelete['id']);

            });

            deleteChosenHintBTN.addEventListener('click', function() {
                if(game_type.value == 'opt1')
                type = "puzzle";

                if(game_type.value == 'opt3')
                 type = "";

                deleteRequestGame(attractionObjToUseInHintDelete['id'],type);
                window.location.href = '/pick_delete_game';
            });
}

function func_to_show(gamesJSON){
     let hint_id_that_was_picked = document.getElementById("write_hint_id_to_delete").value;
   // let number_hint_id = Number(hint_id_that_was_picked);
      gamesJSON.forEach(function (game) {
          // alert("the id is: "+attr['id']);
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if(game['id']==hint_id_that_was_picked)
        {
            let img = document.getElementById('output');
            img.src = game['piecesURLS'];
        }
      });
}

function funcInOrderToDeleteHint(hintsJSON) {
    let hint_id_that_was_picked = document.getElementById("write_hint_id_to_delete").value;
   // let number_hint_id = Number(hint_id_that_was_picked);
      hintsJSON.forEach(function (hint) {
          // alert("the id is: "+attr['id']);
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if(hint['id']==hint_id_that_was_picked)
        {
            //alert("before delete hint!");
            deleteRequestHint(attractionObjToUseInHintDelete['id'],hint['id']);
            window.location.href='/pick_hint_edit';
        }
      });

}

function hint_funcToGetAttraction(attractionsJSON) {
        let name = localStorage.getItem("name_for_add_aq");
        let desc = localStorage.getItem("desc_for_add_aq");
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
        attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description:attr['description']};
       // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if(p.name===name && p.description===desc)
        {
            var textHintToSend = {
            attraction:attr,
            kind:'HT',
            data:document.getElementById("text_hint_id").value
            };
            postRequestHint(textHintToSend,attr['id']);
            window.location.href='/add_hint_edit';
        }
      });

    }

    function getTheAttr(attractionsJSON) {

        let editedPoint = JSON.parse(localStorage.getItem("edited"));
      let lat = editedPoint.lat;
      let lng = editedPoint.lng;
      //let name = "didn't found!!!";
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
      attractionsJSON.forEach(function (attr) {
          // alert("the id is: "+attr['id']);
        let p = {name: attr['name'], description:attr['description'], lat: attr['x'], lng: attr['y']};
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if(p.lat===lat&&(p.lng).toFixed(8)===lng.toFixed(8))
        {
            alert("before delete hint!");
            deleteRequestHint(attr['id'],);
            window.location.href='/pick_hint_edit';
        }
      });
        // alert("cant believe this is happenning!");
    }



function donePickingHints() {
    window.location.href='/attractions';
}


function getRequestGames(funcOnHints,game_type,attr_id){
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    serverRequest("GET", funcOnHints, 'http://'+ip+':12344/managementsystem/attraction/'+ attr_id+
        '/'+game_type+'/?format=json');

    //alert("need to remove this alert and fix funcToGetAttraction()!");
}


function deleteRequestGame(attr_id,game_type){
     serverRequest("DELETE", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+attr_id+'/'+game_type+'/');
    }