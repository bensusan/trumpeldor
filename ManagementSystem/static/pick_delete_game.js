var str;
var str2;
var attractionObjToUseInHintDelete;
let type = "sliding_puzzle";
let game_id_that_was_picked = 0;

function showingSelectOfType() {

    let game_type = document.getElementById("game_type");


    if (game_type.value == 'opt1')
        type = "puzzle";

    getRequestGames(showOpts, type, attractionObjToUseInHintDelete['id']);
}


function showOpts(gamesJSON) {

    let opts = document.getElementById("delete_cb");
    opts.style.display = '';

    let i = 1;
    gamesJSON.forEach(function (game) {
        let d_opt_id = "dcb" + i;

        document.getElementById(d_opt_id).innerText = game['description'];
        document.getElementById(d_opt_id).value = game['id'];
        document.getElementById(d_opt_id).style.display = '';
        i = i + 1;

    });

    var showChosenGameBTN = document.getElementById("show_chosen_game");
    showChosenGameBTN.style.display = '';

    showChosenGameBTN.addEventListener('click', function () {
        game_id_that_was_picked = opts.options[opts.selectedIndex].value;
        getRequestGames(getImageSrcAndShowIt, type, attractionObjToUseInHintDelete['id']);
    });

    var deleteChosenHintBTN = document.getElementById("delete_chosen_hint");
    deleteChosenHintBTN.style.display = "";

    deleteChosenHintBTN.addEventListener('click', function () {
        deleteRequestGame(attractionObjToUseInHintDelete['id'], type);
        window.location.href = '/pick_delete_game';
    });


}

function getImageSrcAndShowIt(gamesJSON) {

    gamesJSON.forEach(function (game) {
        if (game['id'] == game_id_that_was_picked) {
            let picture = game['piecesURLS'][0];
            let image = document.getElementById('output');
            image.src = picture.replace('_01_01','');
        }
    });
}

function funcForExistingHints(attractionsJSON) {

    let name = localStorage.getItem("name_for_add_aq");
    let desc = localStorage.getItem("desc_for_add_aq");
    // alert("in get name! "+"of the origin : " + lat + " , " + lng);
    attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description: attr['description']};
        if (p.name === name && p.description === desc) {
            // getRequestGames(games_func_sliding,"sliding_puzzle",attr['id']);
            // getRequestGames(games_func_drag,"puzzle",attr['id']);
            attractionObjToUseInHintDelete = attr;
        }
    });

}


window.onload = function () {
    let cb = document.getElementById("delete_cb");
    cb.onchange = function () {
        showingSelectOfType();
    };
    getRequestAttractions(funcForExistingHints);
    localFileVideoPlayer();
};

function wantToDeleteButton() {
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

    showChosenHintBTN.addEventListener('click', function () {

        if (game_type.value == 'opt1')
            type = "puzzle";

        getRequestGames(func_to_show, type, attractionObjToUseInHintDelete['id']);

    });

    deleteChosenHintBTN.addEventListener('click', function () {
        if (game_type.value == 'opt1')
            type = "puzzle";

        deleteRequestGame(attractionObjToUseInHintDelete['id'], type);
        window.location.href = '/pick_delete_game';
    });
}

function func_to_show(gamesJSON) {
    let hint_id_that_was_picked = document.getElementById("write_hint_id_to_delete").value;
    // let number_hint_id = Number(hint_id_that_was_picked);
    gamesJSON.forEach(function (game) {

        if (game['id'] == hint_id_that_was_picked) {
            let img = document.getElementById('output');
            img.src = game['piecesURLS'];
        }
    });
}


function getRequestGames(funcOnHints, game_type, attr_id) {
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    syncServerRequest("GET", funcOnHints, 'http://' + ip + ':12344/managementsystem/attraction/' + attr_id +
        '/' + game_type + '/?format=json');

}


function deleteRequestGame(attr_id, game_type) {
    syncServerRequest("DELETE", function noop(dummy) {
    }, 'http://' + ip + ':12344/managementsystem/attraction/' + attr_id + '/' + game_type + '/');
}