window.onload=function () {

	   getRequestAttractions(funcForExistingHints);
		let slidingPuzzleBTN = document.getElementById('sliding_puzzle_button');
        slidingPuzzleBTN.addEventListener('click', function() {
			window.location.href='/add_hint';
        });
};