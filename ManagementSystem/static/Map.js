//from django.conf import settings

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: {lat: 31.262860, lng: 34.801753}
    });

}

function addListener(){
    google.maps.event.addListener(map, 'click', (function(event) {
        if (location.href == 'http://132.72.23.64:12345/managementsystem/main/map/' && currPointClicked) {
            marker.setMap(null);
            pointsForTrack = null;
        }
        currPointClicked = createPoint(event.latLng.lat(), event.latLng.lng());
        markerPoint(currPointClicked);
    }));
}


function markAttraction(pos){
    marker = new google.maps.Marker({
        position: pos,
        map: map
    });
    marker.setMap(map);
}

function markerPoint(p){
    let pointToMarker = {lat: p.lat, lng: p.lng};
    marker = new google.maps.Marker({
        position: pointToMarker,
        map: map
    });
    marker.setMap(map);
}


