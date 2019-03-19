alert("haddddra");
// alert(localStorage.getItem("trying"));

window.onload=function () {

	   getRequestAttractions(funcForExistingHints);
		let slidingPuzzleBTN = document.getElementById('sliding_puzzle_button');
        slidingPuzzleBTN.addEventListener('click', function() {
			window.location.href='/add_hint';
        });
};

// function newPopup(url) {
// 	popupWindow = window.open(
// 		url,'popUpWindow','height=300,width=400,left=10,top=10,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes');
// }

function addGames() {
	alert("not implemented yet!");
}

