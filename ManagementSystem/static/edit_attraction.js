var attr_for_editing;
var helperVar;
var helperVarVid;


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



window.onload=function(){
    getRequestAttractions(getName);
    localFileVideoPlayer();
    };


function uploadVideoBTNclick(){
    	let vid_input = document.getElementById('video_input');
        vid_input.click();
}


function finishEditingAttraction() {
    let attr_after_editing;
    let vidArr = attr_for_editing['videosURLS'];
    if(helperVarVid!=undefined)
    {
        vidArr=[];
        vidArr.push(helperVarVid);
    }

    if(helperVar==undefined) {
        attr_after_editing = {
            name: document.getElementById("attr_name").value,
            x: attr_for_editing['x'],
            y: attr_for_editing['y'],
            description: document.getElementById("desc").value,
            picturesURLS: attr_for_editing['picturesURLS'],
            videosURLS: vidArr
        };
    }
    else {
        let picArr=[];
        picArr.push(helperVar);
        attr_after_editing = {
            name: document.getElementById("attr_name").value,
            x: attr_for_editing['x'],
            y: attr_for_editing['y'],
            description: document.getElementById("desc").value,
            picturesURLS: picArr,
            videosURLS: vidArr
        };
    }
         editRequestAttraction(attr_after_editing,attr_for_editing['id']);
         window.location.href='/attractions';
}


function deletePoint() {
        getRequestAttractions(functionOfDelete);
    }

function functionOfDelete(attractionsJSON) {

    let editedPoint = JSON.parse(localStorage.getItem("edited"));
      let lat = editedPoint.lat;
      let lng = editedPoint.lng;

      attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description:attr['description'], lat: attr['x'], lng: attr['y']};

        if((p.lat).toFixed(8)==lat.toFixed(8)&&(p.lng).toFixed(8)==lng.toFixed(8))
        {
            deleteRequestAttraction(attr['id']);
            window.location.href='/attractions';
        }
      });
    }



    function getName(attractionsJSON){
      // alert("in get name!");
      let editedPoint = JSON.parse(localStorage.getItem("edited"));
      let lat = editedPoint.lat;
      let lng = editedPoint.lng;
      // let name = "didn't found!!!";
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
      attractionsJSON.forEach(function (attr) {
          // alert("the id is: "+attr['id']);
        let p = {id:attr['id'],name: attr['name'], description:attr['description'], lat: attr['x'], lng: attr['y']};
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if(p.lat===lat&&(p.lng).toFixed(8)===lng.toFixed(8))
        {
            attr_for_editing=attr;
          // name=p.name;
          document.getElementById("attr_name").value = p.name;
          document.getElementById("desc").value = p.description;
            var image = document.getElementById('output');
	        image.src = attr['picturesURLS'][0];
	        var video = document.getElementById('vid_itself');
	        video.src = attr['videosURLS'][0];
          localStorage.setItem("name_for_add_aq", p.name);
        localStorage.setItem("desc_for_add_aq", p.description);
        }
      });

      // alert("the name is: "+name);
    }

    function  showVals() {
      getRequestAttractions(getName);
    }

    function editRequestAttraction(attraction,attr_id){
    serverRequest("PUT", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+attr_id+'/',
        JSON.stringify(attraction));
}



function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
	image.src = URL.createObjectURL(element.files[0]);

    helperVar="";

  var file = element.files[0];
  var reader = new FileReader();
  reader.onloadend = function() {
   helperVar=reader.result
  };

  reader.readAsDataURL(file);
}


function encodeVideoFileAsURL(element) {

    helperVarVid="";

  var file = element.files[0];
  var reader = new FileReader();
  reader.onloadend = function() {
   //alert(reader.result)
   helperVarVid=reader.result
  };

  reader.readAsDataURL(file);
}