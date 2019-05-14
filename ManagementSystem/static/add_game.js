
window.onload=function () {
    let p1 = document.getElementById('p1');
    let p2 = document.getElementById('p2');
    let p3 = document.getElementById('p3');
    let sureLBL = document.getElementById('sureLBL');
    let yesBTN = document.getElementById('yesBTN');
    let noBTN = document.getElementById('noBTN');


	    let slidingPuzzleBTN = document.getElementById('sliding_puzzle_button');
        slidingPuzzleBTN.addEventListener('click', function() {
            localStorage.setItem("game_kind","sliding");
            let ref = window.location.href;
            let the_href = ref.split('/')[3];
            localStorage.setItem("last_add_game_url",the_href)
			window.location.href='/add_picture';
        });

        let dragPuzzleBTN = document.getElementById('drag_puzzle_button');
        dragPuzzleBTN.addEventListener('click', function() {
            localStorage.setItem("game_kind","drag");
            let ref = window.location.href;
            let the_href = ref.split('/')[3];
            localStorage.setItem("last_add_game_url",the_href)
			window.location.href='/add_picture';
        });

        let findTheDiffBTN = document.getElementById('find_the_diff');
        findTheDiffBTN.addEventListener('click', function() {
			window.location.href='/add_picture';
        });

        let captureTaskBTN = document.getElementById('capture_task');
        captureTaskBTN.addEventListener('click', function() {
			p1.style.display ='';
			p2.style.display ='';
			p3.style.display ='';
			sureLBL.style.display ='';
			yesBTN.style.display ='';
			noBTN.style.display ='';

            yesBTN.addEventListener('click', function() {
                alert("under construction!!!")
             });

            noBTN.addEventListener('click', function() {
                p1.style.display ='none';
                p2.style.display ='none';
                p3.style.display ='none';
                sureLBL.style.display ='none';
                yesBTN.style.display ='none';
                noBTN.style.display ='none';
             });


        });

var tmuna = document.getElementById("sukablat");
    tmuna.src = localStorage.getItem("url_of_img");
        // var image = document.getElementById('shitfuck');
    	// image.src = URL.createObjectURL(event.target.files[0]);

};
