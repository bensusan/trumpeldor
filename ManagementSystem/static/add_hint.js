var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
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