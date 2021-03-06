//from django.conf import settings
let map;
let curPosClicked;
let curMarker;
let coordinates_of_last_click;
// let points= [
//     {lat: 31.263465932844372, lng: 34.801946282386783},
//     {lat: 31.263065932844372, lng: 34.801146282386783},
//     {lat: 31.263865932844372, lng: 34.802146282386783},
//     {lat: 31.262773527283052, lng: 34.802075028419495}
// ];

let points = JSON.parse(localStorage.getItem("points"));

window.onload = function () {
    let add_manually_menu = document.getElementById('add_manually_menu');
    add_manually_menu.addEventListener('click', function () {
        var the_manual_lat = document.getElementById("manual_lat");
        the_manual_lat.style.display = "inline";

        var the_manual_lng = document.getElementById("manual_lng");
        the_manual_lng.style.display = "inline";

        var add_manually_button = document.getElementById("add_manually");
        add_manually_button.style.display = "inline";
        var place_button = document.getElementById("place");
        place_button.style.display = "inline";
        place_button.addEventListener('click', function () {
            if (the_manual_lng.value != "" && the_manual_lat.value != "") {
                let man_location = positionInMap(parseFloat(the_manual_lat.value), parseFloat(the_manual_lng.value));
                let marker = new google.maps.Marker({
                    position: man_location,
                    map: map
                    , icon: {
                        url: "http://maps.google.com/mapfiles/ms/icons/pink-dot.png"
                    }
                });
                marker.setMap(map);
                map.panTo(man_location);
            }
        });
    });

    let addManuallyBTN = document.getElementById('add_manually');
    addManuallyBTN.addEventListener('click', function () {
        let manualLat = document.getElementById('manual_lat').value;
        let manualLng = document.getElementById('manual_lng').value;
        let pos = {lat: manualLat, lng: manualLng};
        localStorage.setItem("addedPoint", JSON.stringify(pos));
        window.location.href = '/add_attraction';
    });
};

function initMapAndAttractions() {
    initMap();
    initAttractionsMarkers();
}

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: {lat: 31.262860, lng: 34.801753}
    });
    initAttractionsMarkers();
    listenerForMap(map);
    initPoints();

}


function addEditListener(m) {
    m.addListener('click', function () {

        if (prev_m != 1) {

            prev_m.setIcon(prev_icon);
        }
        prev_icon = m.icon;
        m.setIcon("http://maps.google.com/mapfiles/ms/icons/pink-dot.png");

        prev_m = m;

        var editBTN = document.getElementById('edit_attraction');
        editBTN.addEventListener('click', function () {
            localStorage.setItem("edited", JSON.stringify(m.position));
            window.location.href = '/edit_attraction';
        });
    });
}

function listenerForMap(map) {
    google.maps.event.addListener(map, 'click', (function (event) {
        coordinates_of_last_click = event.latLng;
        if (curPosClicked) {
            curMarker.setMap(null);
        }

        curPosClicked = positionInMap(event.latLng.lat(), event.latLng.lng());
        curMarker = markAttraction(curPosClicked);
        var addBTN = document.getElementById('add_attraction');
        addBTN.addEventListener('click', function (event) {
            let pos = {lat: curPosClicked.lat, lng: curPosClicked.lng};
            localStorage.setItem("addedPoint", JSON.stringify(pos));
            window.location.href = '/add_attraction';
        });
    }));
}


function addListenerForMarker(marker) {
    google.maps.event.addListener(marker, 'click', (function (event) {
        return function () {
        }
    })(event));

}

function positionInMap(lat, lng) {
    return {lat: lat, lng: lng};
}

