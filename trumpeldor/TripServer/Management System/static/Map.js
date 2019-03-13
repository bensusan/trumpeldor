let x;
 function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: {lat: 31.262860, lng: 34.801753}
    });
    //initPoints(getAllPoints);
    //addListener();
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

function initPoints(functionOnReady){
          Http.open("GET", attractionsURL);
          Http.send();
          Http.onreadystatechange = functionOnReady;
      }

      function markerPoint(p){
        let pointToMarker = {lat: p.lat, lng: p.lng};
        marker = new google.maps.Marker({
          position: pointToMarker,
          map: map
        });
        marker.setMap(map);
        //  marker.addListener(marker, 'click', function(event) {
        //      alert("fdfdf");
        //   currPointClicked = createPoint(event.latLng.lat(),event.latLng.lng());
        // })
          google.maps.event.addListener(marker, 'click', (function(event) {
              return function() {
                  //    currPointClicked = createPoint(event.latLng.lat(), event.latLng.lng());
                 if(location.href == 'http://132.72.23.64:12345/managementsystem/main/maptrack/'){
                  let bool = checkIfPointInRadius(marker);
                      if(bool > -1) {
                          attrForTrack.push(pointsForTrack[bool]);
                      }
              }
              }
          })(event));

      }


function getAllPoints(e){
          if (Http.readyState == 4 && Http.status == 200) {
                  let response = JSON.parse(Http.responseText);
                  for(let i = 0; i < response.length; i++){
                      points.push({lat : response[i].x, lng : response[i].y});
                      pointsForTrack.push(response[i]);
                  }
                  for(let i = 0; i < points.length; i++){
                      markerPoint(points[i]);
                  }
              }
}
