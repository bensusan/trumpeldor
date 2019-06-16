// const Http = new XMLHttpRequest();

function syncServerRequest(getOrPost, functionOnReady, url, post=null){
    Http.onreadystatechange = function(){
        if(Http.readyState === 4 && Http.status === 200){
            functionOnReady(JSON.parse(Http.responseText));
        }
    };
    Http.open(getOrPost, url, false);
    if(post) {
        Http.setRequestHeader('Content-type','application/json; charset=utf-8');
        Http.send(post);
        window.location.href = '/attractions';
        return false;
    }
    Http.send();
}




