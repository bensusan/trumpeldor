let loadFile = function(event) {
	let image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);

};

function localFileVideoPlayer() {
	'use strict';
  let URL = window.URL || window.webkitURL;
  let displayMessage = function (message, isError) {
    let element = document.querySelector('#message');
    element.innerHTML = message;
    element.className = isError ? 'error' : 'info'
  };
  let playSelectedFile = function (event) {
    let file = this.files[0];
    let type = file.type;
    let videoNode = document.querySelector('video');
    let canPlay = videoNode.canPlayType(type);
    if (canPlay === '') canPlay = 'no';
    let message = 'Can play type "' + type + '": ' + canPlay;
    let isError = canPlay === 'no';
    //displayMessage(message, isError)

    if (isError) {
      return
    }

    let fileURL = URL.createObjectURL(file);
    videoNode.src = fileURL;

  };
  let inputNode = document.querySelector('input');
  inputNode.addEventListener('change', playSelectedFile, false);
}

var attr_for_editing;

window.onload=function(){
    getName();
    var deletePointBTN = document.getElementById('delete_point');
    deletePointBTN.addEventListener('click', function() {
        // alert("clicked delp()");
        getRequestAttractions(functionOfDelete);

    });
    localFileVideoPlayer();
    };


    function finishEditingAttraction() {
        alert("under construction!");
        // editRequestAttraction(attr_for_editing,attr_for_editing['id']);
        // window.location.href='/attractions';
    }


    // function deletePoint() {
    //     getRequestAttractions(functionOfDelete);
    // }

    function functionOfDelete(attractionsJSON) {

        let editedPoint = JSON.parse(localStorage.getItem("edited"));
      let lat = editedPoint.lat;
      let lng = editedPoint.lng;
      //let name = "didn't found!!!";
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
      attractionsJSON.forEach(function (attr) {
          // alert("the id is: "+attr['id']);
        let p = {name: attr['name'], description:attr['description'], lat: attr['x'], lng: attr['y']};
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if(p.lat===lat&&(p.lng).toFixed(8)===lng.toFixed(8))
        {
            // alert("s");
           // deleteRequestAttraction(attr,attr['id']);
            deleteRequestAttraction(attr['id']);
            window.location.href='/attractions';
        }
      });
        // alert("cant believe this is happenning!");
    }


    function getName(attractionsJSON){
      alert("in get name!");
      let editedPoint = JSON.parse(localStorage.getItem("edited"));
      let lat = editedPoint.lat;
      let lng = editedPoint.lng;
      let name = "didn't found!!!";
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
      attractionsJSON.forEach(function (attr) {
          // alert("the id is: "+attr['id']);
        let p = {name: attr['name'], description:attr['description'], lat: attr['x'], lng: attr['y']};
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if(p.lat===lat&&(p.lng).toFixed(8)===lng.toFixed(8))
        {
            attr_for_editing=attr;
          name=p.name;
          document.getElementById("attr_name").value = p.name;
          document.getElementById("desc").value = p.description;
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

    function editRequestAttraction(attraction,attr_id){
    alert("edit blat hui");
    serverRequest("PUT", function noop(dummy){}, 'http://10.0.0.7:12344/managementsystem/attraction/'+attr_id,
        JSON.stringify(attraction));
}