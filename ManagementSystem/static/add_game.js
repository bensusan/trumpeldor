let idOfAttraction = -22;
let curr_url = window.location;

window.onload = function () {
    getRequestAttractions(funcToGetID);
    initializeGamesBTNs();
};

function initializeGamesBTNs() {
    let hebrewBTN = document.getElementById("hebrewBTN");
    let englishBTN = document.getElementById("englishBTN");
    let p1 = document.getElementById('p1');
    let p2 = document.getElementById('p2');
    let p3 = document.getElementById('p3');
    let sureLBL = document.getElementById('sureLBL');
    let yesBTN = document.getElementById('yesBTN');
    let noBTN = document.getElementById('noBTN');
    let photoGameInstructions = document.getElementById('game_instructions_text');
    let photoGameInstructionsEnglish = document.getElementById('game_instructions_text_english');
    let sendPhotoGameBTN = document.getElementById('sendPhotoGame');

    let slidingPuzzleBTN = document.getElementById('sliding_puzzle_button');
    slidingPuzzleBTN.addEventListener('click', function () {
        localStorage.setItem("game_kind", "sliding");
        let ref = window.location.href;
        let the_href = ref.split('/')[3];
        localStorage.setItem("last_add_game_url", the_href);
        window.location.href = '/add_picture';
    });

    let dragPuzzleBTN = document.getElementById('drag_puzzle_button');
    dragPuzzleBTN.addEventListener('click', function () {
        localStorage.setItem("game_kind", "drag");
        let ref = window.location.href;
        let the_href = ref.split('/')[3];
        localStorage.setItem("last_add_game_url", the_href);
        window.location.href = '/add_picture';
    });

    let captureTaskBTN = document.getElementById('capture_task');
    captureTaskBTN.addEventListener('click', function () {

        p1.style.display = '';
        p2.style.display = '';
        p3.style.display = '';
        sureLBL.style.display = '';
        yesBTN.style.display = '';
        noBTN.style.display = '';

        yesBTN.addEventListener('click', function () {
            p1.style.display = 'none';
            p2.style.display = 'none';
            p3.style.display = '';
            sureLBL.style.display = 'none';
            yesBTN.style.display = 'none';
            noBTN.style.display = 'none';
            photoGameInstructions.style.display = '';
            sendPhotoGameBTN.style.display = '';

            hebrewBTN.addEventListener('click', function () {
                photoGameInstructions.style.display = "";
                photoGameInstructionsEnglish.style.display = "none";
            });

            englishBTN.addEventListener('click', function () {
                photoGameInstructions.style.display = "none";
                photoGameInstructionsEnglish.style.display = "";
            });

            sendPhotoGameBTN.addEventListener('click', function () {
                if (idOfAttraction == -22)
                    alert(curr_url);
                else {
                    postRequestPhotoGame({description: photoGameInstructions.value + ';;' + photoGameInstructionsEnglish.value}, idOfAttraction);
                    alert("משימת צילום נוספה בהצלחה !");
                    window.location = curr_url;
                }
            });

        });

        noBTN.addEventListener('click', function () {
            p1.style.display = 'none';
            p2.style.display = 'none';
            p3.style.display = 'none';
            sureLBL.style.display = 'none';
            yesBTN.style.display = 'none';
            noBTN.style.display = 'none';
        });


    });
}

function postRequestPhotoGame(desc, attr_id) {
    syncServerRequest("POST", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/attraction/' +
        attr_id + '/taking_pic/',
        JSON.stringify(desc));
}


function funcToGetID(attractionsJSON) {
    let name = localStorage.getItem("name_for_add_aq");
    let desc = localStorage.getItem("desc_for_add_aq");
    attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description: attr['description']};
        if (p.name === name && p.description === desc) {
            idOfAttraction = attr['id'];
        }
    });

}