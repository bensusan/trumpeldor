// alert(localStorage.getItem("edited"));
// alert(localStorage.getItem("ans1"+localStorage.getItem("editedNum")));
//  document.getElementById("ans2").value = localStorage.getItem("ans21"+localStorage.getItem("editedNum"));


  // document.getElementById("ans1").value = "afddffd";

//     document.getElementById("ans2").value = localStorage.getItem("ans21");
//     document.getElementById("ans3").value = localStorage.getItem("ans31");
//     document.getElementById("ans4").value = localStorage.getItem("ans41");


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
        alert("point:"+localStorage.getItem("addedPoint")+"\n"+
            "name:"+document.getElementById("attr_name").value);
    }
    
    function getName(attractionsJSON){
      alert("in get name!");
      let editedPoint = JSON.parse(localStorage.getItem("edited"));
      let lat = editedPoint.lat;
      let lng = editedPoint.lng;
      let name = "didn't found!!!";
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
      attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], lat: attr['x'], lng: attr['y']};
        alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if(p.lat==lat&&p.lng==lng)
        {
          name=p.name;
        }
      });

      alert("the name is: "+name);
    }

    function  showVals() {
      // document.getElementById("attr_name").value =localStorage.getItem("attr_name"+localStorage.getItem("editedNum"));
      // document.getElementById("desc").value = localStorage.getItem("desc"+localStorage.getItem("editedNum"));
      // document.getElementById("ques").value = localStorage.getItem("ques"+localStorage.getItem("editedNum"));
      // document.getElementById("ans1").value =localStorage.getItem("ans1"+localStorage.getItem("editedNum"));
      // document.getElementById("ans2").value = localStorage.getItem("ans2"+localStorage.getItem("editedNum"));
      // document.getElementById("ans3").value = localStorage.getItem("ans3"+localStorage.getItem("editedNum"));
      // document.getElementById("ans4").value = localStorage.getItem("ans4"+localStorage.getItem("editedNum"));
      //
      // document.getElementById("path_len").value = localStorage.getItem("path_len"+localStorage.getItem("editedNum"));
      // alert(localStorage.getItem("path_len"+localStorage.getItem("editedNum")));
          // localStorage.getItem("path_len"+localStorage.getItem("editedNum"));
      getRequestAttractions(getName);
    }