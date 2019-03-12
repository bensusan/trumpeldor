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
        var numberOfPoints =Number(localStorage.getItem("numberOfPoints"));
        numberOfPoints=numberOfPoints+1;
        localStorage.setItem("numberOfPoints",""+numberOfPoints);
        // alert("1!");
        var currPoints = JSON.parse(localStorage.getItem("points"));
        var addedPoint = JSON.parse(localStorage.getItem("addedPoint"));
        // alert("2!");
        currPoints.push(addedPoint);
        localStorage.setItem("points",JSON.stringify(currPoints));

        numberOfPoints--;
        localStorage.setItem("attr_name"+numberOfPoints, document.getElementById("attr_name").value);
        localStorage.setItem("desc"+numberOfPoints, document.getElementById("desc").value);
        localStorage.setItem("ques"+numberOfPoints, document.getElementById("ques").value);
        localStorage.setItem("ans1"+numberOfPoints, document.getElementById("ans1").value);
        localStorage.setItem("ans2"+numberOfPoints, document.getElementById("ans2").value);
        localStorage.setItem("ans3"+numberOfPoints, document.getElementById("ans3").value);
        localStorage.setItem("ans4"+numberOfPoints, document.getElementById("ans4").value);
        localStorage.setItem("path_len"+numberOfPoints, document.getElementById("path_len").value);

//         var e = document.getElementById("ddlViewBy");
// var strUser = e.options[e.selectedIndex].value;

        window.location.href='/attractions';
        // alert("point:"+localStorage.getItem("addedPoint")+"\n"+
        //     "name:"+document.getElementById("attr_name").value);
    }