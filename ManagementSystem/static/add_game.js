
window.onload=function () {
	    let slidingPuzzleBTN = document.getElementById('sliding_puzzle_button');
        slidingPuzzleBTN.addEventListener('click', function() {
            localStorage.setItem("game_kind","sliding");
			window.location.href='/add_picture';
        });

        let dragPuzzleBTN = document.getElementById('drag_puzzle_button');
        dragPuzzleBTN.addEventListener('click', function() {
            localStorage.setItem("game_kind","drag");
			window.location.href='/add_picture';
        });

        let findTheDiffBTN = document.getElementById('find_the_diff');
        findTheDiffBTN.addEventListener('click', function() {
			window.location.href='/add_picture';
        });

var tmuna = document.getElementById("sukablat");
    tmuna.src = localStorage.getItem("url_of_img");
        // var image = document.getElementById('shitfuck');
    	// image.src = URL.createObjectURL(event.target.files[0]);

};
