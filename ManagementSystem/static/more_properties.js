let theurl = "";
let failurl = "";
let helperVar = "";

function sendThis(arrOfBoundries) {
    let toSend = {
        boundaries: arrOfBoundries,
        logo: [helperVar],
        loginHours: document.getElementById('info_ttl').value,
        successAudio: [theurl],
        failureAudio: [failurl]
    };
    postRequestSettings(toSend);
    window.location.href = '/main';
}

function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
    image.style.display = "";
    image.src = URL.createObjectURL(element.files[0]);

    helperVar = "";

    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        helperVar = reader.result
    };

    reader.readAsDataURL(file);
}

function func(element) {
    var aud = document.getElementById('audio_controls');
    var mp = document.getElementById('attr_sound');
    var inputBar = document.getElementById('inputBar');

    aud.style.display = "inline";
    mp.src = URL.createObjectURL(element.files[0]);
    aud.load();
    inputBar.style.display = "none";
    theurl = "";
    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        theurl = reader.result
    };
    reader.readAsDataURL(file);
}


function funcFail(element) {
    var aud = document.getElementById('audio_controls_fail');
    var mp = document.getElementById('attr_sound_fail');
    var inputBar = document.getElementById('inputBarFail');

    aud.style.display = "inline";
    mp.src = URL.createObjectURL(element.files[0]);
    aud.load();
    inputBar.style.display = "none";
    failurl = "";
    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        failurl = reader.result
    };
    reader.readAsDataURL(file);
}


function postRequestSettings(data) {
    serverRequest("POST", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/settings/',
        JSON.stringify(data));
}
