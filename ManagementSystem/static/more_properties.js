function func(element) {
    var aud = document.getElementById('audio_controls');
    var mp = document.getElementById('attr_sound');
    var inpi = document.getElementById('inpi');

    aud.style.display="inline";
	mp.src = URL.createObjectURL(element.files[0]);
	aud.load();
	inpi.style.display="none";

}

