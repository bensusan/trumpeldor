let helperVar = "";

function sendThis(arrOfBoundries) {
    let boundries = arrOfBoundries;
    if(arrOfBoundries.length != 4){
        boundries = [{lat:document.getElementById('lat1').value,lng:document.getElementById('lng1').value},
        {lat:document.getElementById('lat2').value,lng:document.getElementById('lng2').value},
        {lat:document.getElementById('lat3').value,lng:document.getElementById('lng3').value},
        {lat:document.getElementById('lat4').value,lng:document.getElementById('lng4').value}];
    }
    let scoreRules = handleScoreRules();
    let toSend = {
        boundaries: boundries,
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


function addRow(tableID) {

    var table = document.getElementById(tableID);

    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);

    var colCount = table.rows[0].cells.length;

    for (var i = 0; i < colCount; i++) {

        var newcell = row.insertCell(i);

        newcell.innerHTML = table.rows[0].cells[i].innerHTML;
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
    syncServerRequest("POST", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/settings/',
        JSON.stringify(data));
}
