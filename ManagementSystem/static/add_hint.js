var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};


function finishHint() {
    alert("hint was added successfully!")
    window.location.href='/attractions';
}