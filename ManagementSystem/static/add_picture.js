var helperVar;

window.onload = function () {
    let submitEverything = document.getElementById("submitEverything");
    submitEverything.addEventListener('click', function () {
        sendTheGameData();
    });

    let game_instructions_text = document.getElementById("game_instructions_text");
    let game_instructions_text_english = document.getElementById("game_instructions_text_english");
    let hebrewBTN = document.getElementById("hebrewBTN");
    let englishBTN = document.getElementById("englishBTN");

    hebrewBTN.addEventListener('click', function () {
        game_instructions_text.style.display = "";
        game_instructions_text_english.style.display = "none";
    });

    englishBTN.addEventListener('click', function () {
        game_instructions_text.style.display = "none";
        game_instructions_text_english.style.display = "";
    });
};

function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(element.files[0]);

    helperVar = "";

    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        helperVar = reader.result;
    };

    reader.readAsDataURL(file);
}


function funcToSendGame(attractionsJSON) {

    let name = localStorage.getItem("name_for_add_aq");
    attractionsJSON.forEach(function (attr) {

        let p = {name: attr['name'], description: attr['description']};
        if (p.name === name ) {
            let description = document.getElementById("game_instructions_text").value +
                ";;" + document.getElementById("game_instructions_text_english").value;

            if (helperVar != undefined) {
                // can do it with all pics.. just add loop
                sendLongBase64PartsPic(helperVar);
            }

            if (localStorage.getItem("game_kind") == "sliding") {
                let the_kind = "sliding_puzzle";
                let n_size = document.getElementById("n_size");
                let n_size_val = n_size.options[n_size.selectedIndex].value;
                let data_send = {
                    description: description,
                    piecesURLS: ["hello"], width: n_size_val, height: n_size_val
                };
                localStorage.setItem(name + the_kind, helperVar);
                let attr_id = attr['id'];
                postRequestGame(data_send, attr_id, the_kind);
            }
            if (localStorage.getItem("game_kind") == "drag") {
                let the_kind = "puzzle";
                let n_size = document.getElementById("n_size").value;
                let data_send = {
                    description: description,
                    piecesURLS: ["hello"], width: n_size, height: n_size
                };
                localStorage.setItem(name + the_kind, helperVar);
                let attr_id = attr['id'];
                postRequestGame(data_send, attr_id, the_kind);
            }
            window.location.href = localStorage.getItem("whereToGoInGame");
        }
    });
}

function sendTheGameData() {
    getRequestAttractions(funcToSendGame);
}

function postRequestGame(data, attr_id, game_kind) {
    serverRequest("POST", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/attraction/' +
        attr_id + '/' + game_kind + '/',
        JSON.stringify(data));
}

