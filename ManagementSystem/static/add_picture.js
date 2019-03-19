
var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
    localStorage.setItem("trying", JSON.stringify(image.toString()));
	var editBTN = document.getElementById('newone');
        editBTN.addEventListener('click', function() {
        	var imo = document.getElementById('newone2');
        	// var imo3 = document.getElementById('newone3');
            imo.src=URL.createObjectURL(event.target.files[0]);

            document.getElementById("url_of_pic").innerHTML = URL.createObjectURL(event.target.files[0]);
            // imo3.src=URL.createObjectURL(event.target.files[0]);

        });


};
var suki;

function shit(suk) {
    suki=suk;
    document.getElementById("suka").innerHTML=suki;
    var tmuna = document.getElementById("sukablat");
    tmuna.src = suki;
}


function encodeImageFileAsURL(element) {
    suki="";
  var file = element.files[0];
  var reader = new FileReader();
  reader.onloadend = function() {
   //alert(reader.result)
   shit(reader.result)
  }
  reader.readAsDataURL(file);
}
