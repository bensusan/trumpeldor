let countOfPoints = 1;
let curPosClicked;
let curMarker;
let coordinates_of_last_click;
let arrOfPoints = [];
let map;
//
window.onload = function () {

    let sendSettings = document.getElementById("save_props");
    sendSettings.addEventListener('click', function () {
        sendAllSettingsWithPointArr();
    });

    getRequestSettings(showSettings);

    let ok1 = document.getElementById('ok1');
    let ok2 = document.getElementById('ok2');
    let ok3 = document.getElementById('ok3');
    let ok4 = document.getElementById('ok4');

    ok2.style.display = 'none';
    ok3.style.display = 'none';
    ok4.style.display = 'none';

    ok1.addEventListener('click', function () {
        ok2.style.display = '';
        ok1.style.display = 'none';
        showingPointOnMapAndChooseIt();
    });

    ok2.addEventListener('click', function () {
        ok3.style.display = '';
        ok2.style.display = 'none';
        showingPointOnMapAndChooseIt();
    });

    ok3.addEventListener('click', function () {
        ok4.style.display = '';
        ok3.style.display = 'none';
        showingPointOnMapAndChooseIt();
    });

    ok4.addEventListener('click', function () {
        ok4.style.display = 'none';
        showingPointOnMapAndChooseIt();
    });

};

function showSettings(settingsJSON) {
    let boundaries = settingsJSON['boundaries'];
    document.getElementById('lat1').value = boundaries[0].lat;
    document.getElementById('lng1').value = boundaries[0].lng;
    document.getElementById('lat2').value = boundaries[1].lat;
    document.getElementById('lng2').value = boundaries[1].lng;
    document.getElementById('lat3').value = boundaries[2].lat;
    document.getElementById('lng3').value = boundaries[2].lng;
    document.getElementById('lat4').value = boundaries[3].lat;
    document.getElementById('lng4').value = boundaries[3].lng;


    document.getElementById('info_ttl').value = settingsJSON['loginHours'];
    let rules = settingsJSON['scoreRules'];
    let rulesCount = rules.length;
    let rulesToAdd = rulesCount - 1;
    for (let i = 0; i < rulesToAdd; i++) {
        addRow('ruleTable');
    }
    let tableOfAnswers = document.getElementById('ruleTable');
    let rowsOfTable = tableOfAnswers.rows;
    let numberOfRowsInTable = rowsOfTable.length;
    let rowIteratorIndex;

    for (rowIteratorIndex = 0; rowIteratorIndex < numberOfRowsInTable; rowIteratorIndex++) {
        let rule = rules[rowIteratorIndex].ruleName;
        let score = rules[rowIteratorIndex].score;
        rowsOfTable[rowIteratorIndex].cells[1].childNodes[0].value = score;
        rowsOfTable[rowIteratorIndex].cells[2].childNodes[0].value = rule;
    }
}

function initMapAndAttractionsprop() {
    initMap();
    initAttractionsMarkers();
}

function showingPointOnMapAndChooseIt() {
    let x = document.getElementById('lat' + countOfPoints);
    let y = document.getElementById('lng' + countOfPoints);
    let pointToMark = positionInMap(x.value, y.value);
    arrOfPoints.push(pointToMark);
    markAttraction(pointToMark);
    countOfPoints++;
    markArr();
}

function sendAllSettingsWithPointArr() {
    sendThis(arrOfPoints);
}


function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: {lat: 31.262860, lng: 34.801753}
    });
    // initAttractionsMarkers();
    listenerForMap(map);
    initPoints();
}


function addEditListener(m) {
    m.addListener('click', function () {
        prev_m = m;
    });
}

function listenerForMap(map) {
    google.maps.event.addListener(map, 'click', (function (event) {
        coordinates_of_last_click = event.latLng;

        if (countOfPoints < 5) {
            let x = document.getElementById('lat' + countOfPoints);
            let y = document.getElementById('lng' + countOfPoints);
            x.value = coordinates_of_last_click.lat();
            y.value = coordinates_of_last_click.lng();
        }

        if (curPosClicked) {
            curMarker.setMap(null);
        }
        markArr();
        curPosClicked = positionInMap(event.latLng.lat(), event.latLng.lng());
        curMarker = markAttraction(curPosClicked);
    }));
}


function initAttractionsMarkers() {
    getRequestAttractions(markAttractions);
}

function getRequestAttractions(funcOnAttractions) {
    // the server port and my ip
    serverRequest("GET", funcOnAttractions, 'http://' + ip + ':12344/managementsystem/attraction/?format=json');
}

function markAttractions(attractionsJSON) {
    attractionsJSON.forEach(function (attr) {

        let pos = {lat: attr['x'], lng: attr['y']};
        marker_arr.push(pos);
        localStorage.setItem("title" + pos, "attraction ID: " + attr['id'] +
            "\nattraction name: " + attr['name'] + "\nposition: (" + attr['x'] + "," + attr['y'] + ")");
        markAttraction(pos);
    });
}


function markAttraction(pos) {
    let marker = new google.maps.Marker({
        position: pos,
        map: map,
        icon: {
            url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
        }
    });
    // marker_arr.push(marker);
    marker.setMap(map);
    addEditListener(marker);
    return marker;
}

function positionInMap(lat, lng) {
    return {lat: lat, lng: lng};
}


function markArr() {
    for (let i = 0; i < arrOfPoints.length; i++) {
        let p = arrOfPoints[i];
        markAttraction(p);
    }
}

function getRequestSettings(func) {
    serverRequest("GET", func, 'http://' + ip + ':12344/managementsystem/settings/?format=json');
}