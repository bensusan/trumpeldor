let curPosClicked;
let points_of_longTrack = [];
let pointsOfPath = [];
let pointsOfMedium = [];
let idOfLong = 0;
let fullLongPoints = [];


function initMapAndAttractionss() {
    pointsOfPath = [];

    getRequestTracks(markAttractionsOfLongPaths);
    initMapp();
    initAttractionsMarkersOfLongPath();
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
        var addToPathBTN = document.getElementById('add_reg_to_path_long');
        addToPathBTN.addEventListener('click', function () {
            if (pointsOfPath.indexOf(m.position) == -1 && curPosClicked == m.position) {
                let point_to_push = {lat: m.position.lat(), lng: m.position.lng()};
                pointsOfPath.push(point_to_push);
            }
            getRequestAttractions(needThisToGetPointsIDs);
        });

        var deleteFromPathBTN = document.getElementById('delete_from_path_long');
        deleteFromPathBTN.addEventListener('click', function () {
            let t = 1;
            let point_to_delete2 = {lat: m.position.lat().toFixed(10), lng: m.position.lng().toFixed(10)};
            fullLongPoints.forEach(function (long_point) {
                if ((long_point['x'].toFixed(10) == point_to_delete2.lat) &&
                    (long_point['y'].toFixed(10) == point_to_delete2.lng)) {

                    points_of_longTrack.forEach(function (the_point) {
                        if ((the_point['x'].toFixed(10) == point_to_delete2.lat) &&
                            (the_point['y'].toFixed(10) == point_to_delete2.lng)) {
                            if (t == 1) {
                                t = 122;
                                deletePointFromTrackRequest(long_point['id'], idOfLong);
                            }
                        } else {
                            if (t == 1) {
                                t = 122;
                                alert("אין אפשרות למחוק נקודה ממסלול שאינו ארוך.");
                            }
                        }

                    });

                }
            });
            window.location.href = '/edit_long_path';

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


function markAttractionsOfLongPaths(tracksJSON) {

    tracksJSON.forEach(function (track) {

        if (track['length'] == 3) {
            idOfLong = track['id'];
            points_of_longTrack = track['points'];
            let points_of_track = track['points'];
            let points_of_subtrack = track['subTrack']['points'];
            let points_of_subsubtrack = track['subTrack']['subTrack']['points'];
            let children = [].concat(points_of_subtrack, points_of_track, points_of_subsubtrack);

            children.forEach(function (attr) {
                fullLongPoints.push(attr);
                let pos2 = {lat: (attr['x']).toFixed(8), lng: (attr['y']).toFixed(8)}; // change to 13 instead of 8!!!
                let pos = {lat: attr['x'], lng: attr['y']};
                pointsOfMedium.push(pos2);
                localStorage.setItem("title" + pos, "attraction ID: " + attr['id'] + "\nattraction name: " + attr['name'] + "\nposition: (" + attr['x'] + "," + attr['y'] + ")");
                markAttractionOfLongPath(pos);

            })
        }

    });
    getRequestAttractions(markAttractionsOfLongPath_left);

}

function markAttractionsOfLongPath_left(attractionsJSON) {

    attractionsJSON.forEach(function (attr) {

        let pos = {lat: attr['x'], lng: attr['y']};
        let pos2 = {lat: (attr['x']).toFixed(8), lng: (attr['y']).toFixed(8)};// change to 13 instead of 8!!!

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
    var finishBTN = document.getElementById('finish_reg_long');
    finishBTN.addEventListener('click', function () {
        window.location.href = '/main'
    });
}

function needThisToGetPointsIDs(attractionsJSON) {

    attractionsJSON.forEach(function (attr) {
        let attr_point = {x: (attr['x']).toFixed(13), y: (attr['y']).toFixed(13)};
        let attr_id = attr['id'];
        pointsOfPath.forEach(function (point) {
            let the_point = {x: (point.lat).toFixed(13), y: (point.lng).toFixed(13)};
            if ((attr_point.x == the_point.x) && (attr_point.y == the_point.y)) {
                addPointToTrackRequest(attr_id, idOfLong);
            }
        });
    });
    window.location.href = '/edit_long_path';
}


function markAttractionOfLongPath(pos) {
    let the_title = localStorage.getItem("title" + pos);
    let marker = new google.maps.Marker({
        position: pos,
        map: map,
        title: the_title
        , icon: {
            url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
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

function initAttractionsMarkersOfLongPath() {
    getRequestTracks(markAttractionsOfLongPaths);
}


function getRequestTracks(funcOnTrack) {
    syncServerRequest("GET", funcOnTrack, 'http://' + ip + ':12344/managementsystem/track/?format=json');
}

function addPointToTrackRequest(id_of_point_to_add, track_id) {
    syncServerRequest("PUT", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/track/' + track_id + '/add',
        JSON.stringify(id_of_point_to_add));
}

function deletePointFromTrackRequest(id_of_point_to_del, track_id) {
    syncServerRequest("PUT", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/track/' + track_id + '/del',
        JSON.stringify(id_of_point_to_del));
}