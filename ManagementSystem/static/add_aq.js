let arrOfAnswers = [];
let correctAnswersIndexes = [];

window.onload = function () {

    let ques = document.getElementById('ques');
    let quesEnglish = document.getElementById('quesEnglish');
    let tableOfAnswers = document.getElementById('dataTable');
    let tableOfAnswersEnglish = document.getElementById('dataTableEnglish');
    let hebrewBTN = document.getElementById("hebrewBTN");
    let englishBTN = document.getElementById("englishBTN");

    hebrewBTN.addEventListener('click', function () {
        tableOfAnswers.style.display = "";
        tableOfAnswersEnglish.style.display = "none";
        ques.style.display = "";
        quesEnglish.style.display = "none";
    });

    englishBTN.addEventListener('click', function () {
        tableOfAnswers.style.display = "none";
        tableOfAnswersEnglish.style.display = "";
        ques.style.display = "none";
        quesEnglish.style.display = "";
    });


    initializeFinishBTNfunctionality();

};

function initializeFinishBTNfunctionality() {
    let addAqBTN = document.getElementById('finish_add_aq_btn');

    addAqBTN.addEventListener('click', function () {

        let tableOfAnswers = document.getElementById('dataTable');
        let rowsOfTable = tableOfAnswers.rows;
        let numberOfRowsInTable = rowsOfTable.length;
        let rowIteratorIndex;
        let tableOfAnswersEnglish = document.getElementById('dataTableEnglish');
        let rowsOfTableEnglish = tableOfAnswersEnglish.rows;


        for (rowIteratorIndex = 0; rowIteratorIndex < numberOfRowsInTable; rowIteratorIndex++) {
            let answer = rowsOfTable[rowIteratorIndex].cells[1].childNodes[0].value;
            let answerEnglish = rowsOfTableEnglish[rowIteratorIndex].cells[1].childNodes[0].value;
            let isChecked = rowsOfTable[rowIteratorIndex].cells[0].childNodes[0].checked;
            arrOfAnswers.push(answer + ";;" + answerEnglish);

            if (isChecked == true) {
                correctAnswersIndexes.push(rowIteratorIndex + 1);
            }
        }


        getRequestAttractions(funcToGetAttraction);
    });
}

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


function postRequestAmericanQuestion(aq, attr_id) {
    //alert("aq blat");
    serverRequest("POST", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/attraction/' +
        attr_id + '/aquestion/',
        JSON.stringify(aq));
}

function funcToGetAttraction(attractionsJSON) {

    let name = localStorage.getItem("name_for_add_aq");
    let desc = localStorage.getItem("desc_for_add_aq");
    // alert("in get name! "+"of the origin : " + lat + " , " + lng);
    attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description: attr['description']};
        // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if (p.name === name && p.description === desc) {

            let american_question_to_send = {
                question: document.getElementById("ques").value+";;"+document.getElementById("quesEnglish").value
                , answers: arrOfAnswers
                , indexOfCorrectAnswer: correctAnswersIndexes
                , attraction: attr['id'] //atraction id needs to be here
            };
            postRequestAmericanQuestion(american_question_to_send, attr['id']);
            localStorage.setItem("the_attr", JSON.stringify(attr));
        }
    });

    window.location.href = '/add_hint';
}



