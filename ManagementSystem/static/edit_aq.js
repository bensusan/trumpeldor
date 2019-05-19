let arrOfAnswers = [];
let correctAnswersIndexes = [];
let idOfQuestion = localStorage.getItem("aq_id_to_edit");
let idOfAttraction = localStorage.getItem("attr_id_for_aq_edit");


window.onload = function() {

    let addAqBTN = document.getElementById('finish_add_aq_btn');
    getRequestAmericanQuestion(decideFunc,idOfAttraction,idOfQuestion);
    addAqBTN.addEventListener('click', function() {

        let tableOfAnswers = document.getElementById('dataTable');
        let rowsOfTable = tableOfAnswers.rows;
        let numberOfRowsInTable = rowsOfTable.length;
        let rowIteratorIndex;

        for(rowIteratorIndex=0; rowIteratorIndex<numberOfRowsInTable; rowIteratorIndex++)
        {
            let answer = rowsOfTable[rowIteratorIndex].cells[1].childNodes[0].value;
            let isChecked = rowsOfTable[rowIteratorIndex].cells[0].childNodes[0].checked;
            arrOfAnswers.push(answer);

            if(isChecked == true)
            {
                correctAnswersIndexes.push(rowIteratorIndex+1);
            }
        }

        // alert("ans: "+arrOfAnswers +" indexes: "+correctAnswersIndexes);

    getRequestAttractions(funcToGetAttraction);
    });

};

function decideFunc(aqJSON) {
    let question = aqJSON['question'];
    let answersArr = aqJSON['answers'];
    let indexesArr = aqJSON['indexOfCorrectAnswer'];
    let currentNumberOfRows = 3;
    let howMuchRowsToAdd = answersArr.length - currentNumberOfRows;

    while (howMuchRowsToAdd>0){
        addRow('dataTable');
        howMuchRowsToAdd--;
    }

    let questionElement = document.getElementById('ques');
    questionElement.value = question;

    let tableOfAnswers = document.getElementById('dataTable');
    let rowsOfTable = tableOfAnswers.rows;
    let numberOfRowsInTable = rowsOfTable.length;
    let rowIteratorIndex;

    for(rowIteratorIndex=0; rowIteratorIndex<numberOfRowsInTable; rowIteratorIndex++)
    {
        rowsOfTable[rowIteratorIndex].cells[1].childNodes[0].value = answersArr[rowIteratorIndex];

        if(indexesArr.includes(rowIteratorIndex))
        {
            rowsOfTable[rowIteratorIndex].cells[0].childNodes[0].checked = true;
        }
    }


}

function addRow(tableID) {

			var table = document.getElementById(tableID);

			var rowCount = table.rows.length;
			var row = table.insertRow(rowCount);

			var colCount = table.rows[0].cells.length;

			for(var i=0; i<colCount; i++) {

				var newcell	= row.insertCell(i);

				newcell.innerHTML = table.rows[0].cells[i].innerHTML;
				//alert(newcell.childNodes);
				switch(newcell.childNodes[0].type) {
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


function postRequestAmericanQuestion(aq,attr_id){
    //alert("aq blat");
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+
        attr_id+'/aquestion/',
        JSON.stringify(aq));
}

function getRequestAmericanQuestion(funcOnAq,attr_id,aq_id){
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    serverRequest("GET", funcOnAq, 'http://'+ip+':12344/managementsystem/attraction/'+ attr_id+
        '/aquestion/'+aq_id+'/'+'?format=json');
    //alert("need to remove this alert and fix funcToGetAttraction()!");
}

 function funcToGetAttraction(attractionsJSON) {

        let name = localStorage.getItem("name_for_add_aq");
        let desc = localStorage.getItem("desc_for_add_aq");
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
        attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description:attr['description']};
       // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if(p.name===name && p.description===desc)
        {

            let american_question_to_send = {
                    question :document.getElementById("ques").value
                    ,answers: arrOfAnswers
                    ,indexOfCorrectAnswer: correctAnswersIndexes
                    ,attraction:attr['id'] //atraction id needs to be here
            };
            postRequestAmericanQuestion(american_question_to_send,attr['id']);
            localStorage.setItem("the_attr", JSON.stringify(attr));
        }
      });

 window.location.href='/add_hint';
    }


