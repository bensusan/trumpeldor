
window.onload=function () {
	    let slidingPuzzleBTN = document.getElementById('sliding_puzzle_button');
        slidingPuzzleBTN.addEventListener('click', function() {
			window.location.href='/add_picture';
        });

var tmuna = document.getElementById("sukablat");
    tmuna.src = localStorage.getItem("url_of_img");
        // var image = document.getElementById('shitfuck');
    	// image.src = URL.createObjectURL(event.target.files[0]);

};
