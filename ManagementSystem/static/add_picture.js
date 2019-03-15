alert("sda");

var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);

	var editBTN = document.getElementById('newone');
        editBTN.addEventListener('click', function() {
        	var imo = document.getElementById('newone2');
        	// var imo3 = document.getElementById('newone3');
            imo.src=URL.createObjectURL(event.target.files[0]);
            document.getElementById("url_of_pic").innerHTML = URL.createObjectURL(event.target.files[0]);
            // imo3.src=URL.createObjectURL(event.target.files[0]);
        });
};
