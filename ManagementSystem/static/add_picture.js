
var suki;


function shit(suk) {
    suki=suk;
    document.getElementById("suka").innerHTML=suki;
    localStorage.setItem("url_of_img",suki);
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
  }
  
  reader.readAsDataURL(file);
}
