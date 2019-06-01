let theurl = "";


function sendThis() {
    let toSend = {
        boundaries: [],
        logo: [],
        loginHours: document.getElementById('info_ttl').value,
        successAudio: [],
        failureAudio: []
    };
    postRequestSettings(toSend);
    window.location.href = '/main';
}

function func(element) {
    var aud = document.getElementById('audio_controls');
    var mp = document.getElementById('attr_sound');
    var inpi = document.getElementById('inpi');

    aud.style.display = "inline";
    mp.src = URL.createObjectURL(element.files[0]);
    aud.load();
    inpi.style.display = "none";

    theurl = "";

    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        //alert(reader.result)
        doSomething(reader.result)
    };

    reader.readAsDataURL(file);

}

function doSomething(thing) {
    theurl = thing;
}

function postRequestSettings(data) {
    serverRequest("PUT", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/settings/',
        JSON.stringify(data));
}