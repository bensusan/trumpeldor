let theurl = "";
let failurl = "";
let helperVar = "";

function sendThis(arrOfBoundries) {

    let scoreRules = handleScoreRules();
    let toSend = {
        boundaries: arrOfBoundries,
        loginHours: document.getElementById('info_ttl').value,
        scoreRules: scoreRules
    };
    postRequestSettings(toSend);
    window.location.href = '/main';
}

function handleScoreRules() {
    let tableOfAnswers = document.getElementById('ruleTable');
    let rowsOfTable = tableOfAnswers.rows;
    let numberOfRowsInTable = rowsOfTable.length;
    let rowIteratorIndex;
    let scoreRules = [];

    for (rowIteratorIndex = 0; rowIteratorIndex < numberOfRowsInTable; rowIteratorIndex++) {
        let score = rowsOfTable[rowIteratorIndex].cells[1].childNodes[0].value;
        let rule = rowsOfTable[rowIteratorIndex].cells[2].childNodes[0].value;
        let scoreRule = {ruleName: rule, score: score};
        scoreRules.push(scoreRule);
    }
    return scoreRules;
}

function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
    image.style.display = "";
    image.src = URL.createObjectURL(element.files[0]);

    helperVar = "";

    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        helperVar = reader.result
    };

    reader.readAsDataURL(file);
}

// function func(element) {
//     var aud = document.getElementById('audio_controls');
//     var mp = document.getElementById('attr_sound');
//     var inputBar = document.getElementById('inputBar');
//
//     aud.style.display = "inline";
//     mp.src = URL.createObjectURL(element.files[0]);
//     aud.load();
//     inputBar.style.display = "none";
//     theurl = "";
//     var file = element.files[0];
//     var reader = new FileReader();
//     reader.onloadend = function () {
//         theurl = reader.result
//     };
//     reader.readAsDataURL(file);
// }
//


function addRow(tableID) {

    var table = document.getElementById(tableID);

    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);

    var colCount = table.rows[0].cells.length;

    for (var i = 0; i < colCount; i++) {

        var newcell = row.insertCell(i);

        newcell.innerHTML = table.rows[0].cells[i].innerHTML;
        //alert(newcell.childNodes);
        switch (newcell.childNodes[0].type) {
            case "text":
                newcell.childNodes[0].value = "";
                break;
            case "checkbox":
                newcell.childNodes[0].checked = false;
                break;
            case "select-one":
                newcell.childNodes[0].selectedIndex = 0;
                break;
        }
    }
}

function deleteRow(tableID) {
    try {
        var table = document.getElementById(tableID);
        var rowCount = table.rows.length;

        for (var i = 0; i < rowCount; i++) {
            var row = table.rows[i];
            var chkbox = row.cells[0].childNodes[0];
            if (null != chkbox && true == chkbox.checked) {
                if (rowCount <= 1) {
                    alert("Cannot delete all the rows.");
                    break;
                }
                table.deleteRow(i);
                rowCount--;
                i--;
            }


        }
    } catch (e) {
        alert(e);
    }
}

function postRequestSettings(data) {
    serverRequest("POST", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/settings/',
        JSON.stringify(data));
}
