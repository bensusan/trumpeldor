var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};

window.onload = function () {
var textHintBTN = document.getElementById('add_text_hint');
        textHintBTN.addEventListener('click', function() {
            alert("yo");
            var textLine = document.getElementById("text_hint_id");
            textLine.style.display = "inline";
        });

var picHintBTN = document.getElementById('add_pic_hint');
        picHintBTN.addEventListener('click', function() {

        });

var vidHintBTN = document.getElementById('add_vid_hint');
        vidHintBTN.addEventListener('click', function() {

        });

};



function finishHint() {
    alert("hint was added successfully!");
    // let data=document.getElementById("data").value;
    // let hint_to_send = {
    //         attraction:"" //atraction id needs to be here
    //     ,kind:
    //     ,data:
    // };
        // postRequestHint(hint_to_send);

    window.location.href='/attractions';
}