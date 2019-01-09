
function addTrack(){
    initPoints(getAllPoints);
     trackToAdd = {subTrack: null, points:attrForTrack, length:0};
    Http.open("POST", tracksURL, true);
Http.setRequestHeader('Content-type','application/json; charset=utf-8');
Http.onload = function () {
    alert(trackToAdd.points +" ");

}
Http.send(JSON.stringify(trackToAdd));
}