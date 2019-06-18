let curPosClicked;

let pointsOfPath = [];
let pointsOfShort = [];
let pointsOfMedium = [];
let idOfMedium = 0;
let idOfLong = 0;


function initMapAndAttractionss() {
    pointsOfPath = [];

    getRequestTracks(markAttractionsOfMediumPaths);
    initMapp();
    initAttractionsMarkersOfMediumPath();
}

function addEditListenerr(m) {
    m.addListener('click', function () {
        if (prev_m != 1) {

            prev_m.setIcon(prev_icon);
        }
        prev_icon = m.icon;
        m.setIcon("http://maps.google.com/mapfiles/ms/icons/pink-dot.png");

        prev_m = m;
        curPosClicked = m.position;
        var addToPathBTN = document.getElementById('add_reg_to_path_med');
        addToPathBTN.addEventListener('click', function () {

            if (pointsOfPath.indexOf(m.position) == -1 && curPosClicked == m.position) {
                let point_to_push = {lat: m.position.lat(), lng: m.position.lng()};
                pointsOfPath.push(point_to_push);
            }
            getRequestAttractions(needThisToGetPointsIDs);
        });
    });
}

function initMapp() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: {lat: 31.262860, lng: 34.801753}
    });
    listenerForMappo();
}


function markAttractionsOfMediumPaths(tracksJSON) {

    tracksJSON.forEach(function (track) {

        if (track['length'] == 2) {
            idOfMedium = track['id'];

            let points_of_track = track['points'];
            let points_of_subtrack = track['subTrack']['points'];
            let children = [].concat(points_of_subtrack, points_of_track);

            children.forEach(function (attr) {
                let pos = {lat: attr['x'], lng: attr['y']};
                let pos2 = {lat: (attr['x']).toFixed(8), lng: (attr['y']).toFixed(8)};
                pointsOfMedium.push(pos2);
                localStorage.setItem("title" + pos, "attraction ID: " + attr['id'] + "\nattraction name: " + attr['name'] + "\nposition: (" + attr['x'] + "," + attr['y'] + ")");
                markAttractionOfMediumPath(pos);
            })
        }

        if (track['length'] == 1) {
            let points_of_track = track['points'];
            points_of_track.forEach(function (attr) {
                let pos2 = {lat: (attr['x']).toFixed(8), lng: (attr['y']).toFixed(8)};
                pointsOfShort.push(pos2);
            })
        }

        if (track['length'] == 3) {
            idOfLong = track['id'];
        }
    });
    getRequestAttractions(markAttractionsOfMediumPath_left);
}

function markAttractionsOfMediumPath_left(attractionsJSON) {

    attractionsJSON.forEach(function (attr) {

        let pos = {lat: attr['x'], lng: attr['y']};
        let pos2 = {lat: (attr['x']).toFixed(8), lng: (attr['y']).toFixed(8)};

        let lats = pointsOfMedium.map(function (x) {
            return (x.lat)
        });
        let lngs = pointsOfMedium.map(function (x) {
            return (x.lng)
        });
        let firstBool = lats.includes(pos2.lat);
        let secondBool = lngs.includes(pos2.lng);
        if (!(firstBool && secondBool)) {
            localStorage.setItem("title" + pos, "attraction ID: " + attr['id'] + "\nattraction name: " + attr['name'] + "\nposition: (" + attr['x'] + "," + attr['y'] + ")");
            markAttractionElse(pos);
        }
    });
}

function listenerForMappo() {
    var finishBTN = document.getElementById('finish_reg_med');
    finishBTN.addEventListener('click', function () {

        getRequestAttractions(needThisToGetPointsIDs);

    });
}

function needThisToGetPointsIDs(attractionsJSON) {
    attractionsJSON.forEach(function (attr) {
        let attr_point = {x: (attr['x']).toFixed(13), y: (attr['y']).toFixed(13)};
        let attr_id = attr['id'];

        pointsOfPath.forEach(function (point) {
            let the_point = {x: (point.lat).toFixed(13), y: (point.lng).toFixed(13)};
            if ((attr_point.x == the_point.x) && (attr_point.y == the_point.y)) {
                addPointToTrackRequest(attr_id, idOfMedium);
            }
        });
    });

    window.location.href = '/add_medium_path';
}

function markAttractionOfMediumPath(pos) {
    let the_title = localStorage.getItem("title" + pos);
    let marker = new google.maps.Marker({
        position: pos,
        map: map,
        title: the_title
        , icon: {
            url: "http://maps.google.com/mapfiles/ms/icons/orange-dot.png"
            // https://medium.com/@letian1997/how-to-change-javascript-google-map-marker-color-8a72131d1207
        }
    });
    marker.setMap(map);
    addEditListenerr(marker);
    return marker;
}

function markAttractionElse(pos) {
    let the_title = localStorage.getItem("title" + pos);
    let marker = new google.maps.Marker({
        position: pos,
        map: map,
        title: the_title
        , icon: {
            url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
        }
    });
    marker.setMap(map);
    addEditListenerr(marker);
    return marker;
}

function initAttractionsMarkersOfMediumPath() {
    getRequestTracks(markAttractionsOfMediumPaths);
}


function getRequestTracks(funcOnTrack) {
    // serverRequest("GET", funcOnAttractions, 'http://192.168.1.12:12344/managementsystem/attraction/?format=json');
    // the server port and my ip
    serverRequest("GET", funcOnTrack, 'http://' + ip + ':12344/managementsystem/track/?format=json');

}

function addPointToTrackRequest(id_of_point_to_add, track_id) {
    syncServerRequest("PUT", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/track/' + track_id + '/add',
        JSON.stringify(id_of_point_to_add));
}