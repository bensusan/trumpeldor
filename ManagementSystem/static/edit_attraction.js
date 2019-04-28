var attr_for_editing;
var suki;
var sukiVid;


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
    // var deletePointBTN = document.getElementById('delete_point');
    // deletePointBTN.addEventListener('click', function() {
    //     getRequestAttractions(functionOfDelete);
    // });
    localFileVideoPlayer();
    };


function doVideo(){
    	let vid_input = document.getElementById('video_input');
        vid_input.click();
}

    function finishEditingAttraction() {
    let attr_after_editing;
    let vidArr = attr_for_editing['videosURLS'];
    if(sukiVid!=undefined)
    {
        vidArr=[];
        vidArr.push(sukiVid);
    }

    if(suki==undefined) {
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
        picArr.push(suki);
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

    function deletePoint2() {
        getRequestAttractions(functionOfDelete2);
    }

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
        if((p.lat).toFixed(8)==lat.toFixed(8)&&(p.lng).toFixed(8)==lng.toFixed(8))
        {
            // alert("s");
           // deleteRequestAttraction(attr,attr['id']);
            deleteRequestAttraction(attr['id']);
            window.location.href='/attractions';
        }
      });
        // alert("cant believe this is happenning!");
    }

    function functionOfDelete2(attractionsJSON) {

        let editedPoint = JSON.parse(localStorage.getItem("edited"));
      let lat = editedPoint.lat;
      let lng = editedPoint.lng;
      //let name = "didn't found!!!";
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
      attractionsJSON.forEach(function (attr) {
          // alert("the id is: "+attr['id']);
        let p = {name: attr['name'], description:attr['description'], lat: attr['x'], lng: attr['y']};
        // alert("in get name! "+"of the origin : " + lat + " , " + lng + "\n of the other: "+p.lat +" , "+ p.lng);
        if((p.lat).toFixed(8)==lat.toFixed(8)&&(p.lng).toFixed(8)==lng.toFixed(8))
        {
            // alert("s");
           // deleteRequestAttraction(attr,attr['id']);
            deleteRequestAttraction(attr['id']);
        }
      });
        // alert("cant believe this is happenning!");
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
        let p = {name: attr['name'], description:attr['description'], lat: attr['x'], lng: attr['y']};
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
   // alert("edit blat hui");
    serverRequest("PUT", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+attr_id+'/',
        JSON.stringify(attraction));
}




function shit(suk) {
    suki=suk;
    document.getElementById("suka").innerHTML=suki;
    localStorage.setItem("url_of_img",suki);
    // var tmuna = document.getElementById("sukablat");
    // tmuna.src = suki;
}

function shitVid(suk) {
    sukiVid=suk;
    // var tmuna = document.getElementById("sukablat");
    // tmuna.src = suki;
}

function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
	image.src = URL.createObjectURL(element.files[0]);

    suki="";

  var file = element.files[0];
  var reader = new FileReader();
  reader.onloadend = function() {
   //alert(reader.result)
   shit(reader.result)
  };

  reader.readAsDataURL(file);
}


function encodeVideoFileAsURL(element) {

    sukiVid="";

  var file = element.files[0];
  var reader = new FileReader();
  reader.onloadend = function() {
   //alert(reader.result)
   shitVid(reader.result)
  };

  reader.readAsDataURL(file);
}