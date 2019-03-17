// alert(localStorage.getItem("addedPoint"));


var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};

window.onload=function(){
(function localFileVideoPlayer() {
	'use strict'
  var URL = window.URL || window.webkitURL
  var displayMessage = function (message, isError) {
    var element = document.querySelector('#message')
    element.innerHTML = message
    element.className = isError ? 'error' : 'info'
  }
  var playSelectedFile = function (event) {
    var file = this.files[0]
    var type = file.type
    var videoNode = document.querySelector('video')
    var canPlay = videoNode.canPlayType(type)
    if (canPlay === '') canPlay = 'no'
    var message = 'Can play type "' + type + '": ' + canPlay
    var isError = canPlay === 'no'
    //displayMessage(message, isError)

    if (isError) {
      return
    }

    var fileURL = URL.createObjectURL(file)
    videoNode.src = fileURL

  }
  var inputNode = document.querySelector('input')
  inputNode.addEventListener('change', playSelectedFile, false)
})()

    }

    function showDataCollected() {
        // var numberOfPoints =Number(localStorage.getItem("numberOfPoints"));
        // numberOfPoints=numberOfPoints+1;
        // localStorage.setItem("numberOfPoints",""+numberOfPoints);
        // // alert("1!");
        // var currPoints = JSON.parse(localStorage.getItem("points"));
        // localStorage.setItem("points",JSON.stringify(currPoints));

        // numberOfPoints--;
        // localStorage.setItem("attr_name"+numberOfPoints, document.getElementById("attr_name").value);
        // localStorage.setItem("desc"+numberOfPoints, document.getElementById("desc").value);
        // localStorage.setItem("ques"+numberOfPoints, document.getElementById("ques").value);
        // localStorage.setItem("ans1"+numberOfPoints, document.getElementById("ans1").value);
        // localStorage.setItem("ans2"+numberOfPoints, document.getElementById("ans2").value);
        // localStorage.setItem("ans3"+numberOfPoints, document.getElementById("ans3").value);
        // localStorage.setItem("ans4"+numberOfPoints, document.getElementById("ans4").value);
        // localStorage.setItem("path_len"+numberOfPoints, document.getElementById("path_len").value);
        //
        // var shortPath = JSON.parse(localStorage.getItem("short_path"));
        // var medPath = JSON.parse(localStorage.getItem("medium_path"));
        // var longPath = JSON.parse(localStorage.getItem("long_path"));
        //
        //
        //   longPath.push(addedPoint);
        //   localStorage.setItem("long_path", JSON.stringify(longPath));
        //
        //
        //   if(document.getElementById("path_len").value=="short") {
        //     shortPath.push(addedPoint);
        //     localStorage.setItem("short_path", JSON.stringify(shortPath));
        //     medPath.push(addedPoint);
        //     localStorage.setItem("medium_path", JSON.stringify(medPath));
        // }
        //
        //   if(document.getElementById("path_len").value=="medium") {
        //     medPath.push(addedPoint);
        //     localStorage.setItem("medium_path", JSON.stringify(medPath));
        // }
        //
        //   let shortPath1 = JSON.parse(localStorage.getItem("short_path"));
        // let medPath1 = JSON.parse(localStorage.getItem("medium_path"));
        // let longPath1 = JSON.parse(localStorage.getItem("long_path"));
        //   alert("short:"+shortPath1.length +"\nmedium: "+medPath1.length +"\nlong: "+longPath1.length);

//         var e = document.getElementById("ddlViewBy");
// var strUser = e.options[e.selectedIndex].value;

        let addedPoint = JSON.parse(localStorage.getItem("addedPoint"));
        // alert("is what: "+ addedPoint.lat +", " + addedPoint.lng + ", "+ (typeof addedPoint.lng));
        // alert("2!");
        // currPoints.push(addedPoint);
        let lat = addedPoint.lat;
        let lang = addedPoint.lng;
        let attraction_to_send = {
            name:document.getElementById("attr_name").value
            //,x:31.262860,y:34.801753
            ,x:lat ,y:lang
            ,description:document.getElementById("desc").value
            ,picturesURLS:[],videosURLS:[]};
        postRequestAttraction(attraction_to_send);
        localStorage.setItem("name_for_add_aq", attraction_to_send.name);
        localStorage.setItem("desc_for_add_aq", attraction_to_send.description);
        window.location.href='/add_game';
        // window.location.href='/attractions';
        // alert("point:"+localStorage.getItem("addedPoint")+"\n"+
        //     "name:"+document.getElementById("attr_name").value);
    }

    function check(){

    alert("ayooooooooo");

    }