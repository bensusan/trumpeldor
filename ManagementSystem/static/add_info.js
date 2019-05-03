window.onload = function () {
    createEditableSelect(document.forms[0].myText);
    getRequestInfo(func_to_show_info);
};

let info_txt;


function func_to_show_info(infoJSON) {
    infoJSON.forEach(function (info) {
        info_txt = info['info'];
    });
    let txt = document.getElementById('subject');
    txt.value=info_txt;
}

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

function getRequestInfo(func){
    // the server port and my ip
    serverRequest("GET", func, 'http://'+ip+':12344/managementsystem/info/?format=json');
}

function postRequestInfo(info){
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/info/',
        JSON.stringify(info));
}
