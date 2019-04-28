function clearText(){
    let txt = document.getElementById('subject');
    txt.value="";
}

function sendInfo(){
    let txt = document.getElementById('subject').value;
    let inf = {info:txt};
    postRequestInfo(inf);
    window.location.href ='/main';
}

function postRequestInfo(info){
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/info/',
        JSON.stringify(info));
}