
var suki;


function shit(suk) {
    suki=suk;
    document.getElementById("suka").innerHTML=suki;
    localStorage.setItem("url_of_img",suki);
    // var tmuna = document.getElementById("sukablat");
    // tmuna.src = suki;
}


function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
	image.src = URL.createObjectURL(element.files[0]);

    suki="";

  var file = element.files[0];
  var reader = new FileReader();
  reader.onloadend = function() {
   //alert(reader.result)
   shit(reader.result)
  }

  reader.readAsDataURL(file);
}

function funcToSendGame(attractionsJSON) {
        let name = localStorage.getItem("name_for_add_aq");
        let desc = localStorage.getItem("desc_for_add_aq");
      // alert("in get name! "+"of the origin : " + lat + " , " + lng);
        attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description:attr['description']};
       // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if(p.name===name && p.description===desc)
        {

            if(localStorage.getItem("game_kind")=="sliding") {
                let the_kind = "sliding_puzzle";
                let n_size = document.getElementById("n_size").value;
                let data_send = {piecesURLS: suki, width: n_size, height: n_size, description: document.getElementById("game_instructions_text").value};
                let attr_id = attr['id'];
                postRequestGame(data_send,attr_id,the_kind);
            }
            window.location.href='/'+localStorage.getItem("last_add_game_url"); ////////////////////////////change to both
        }


    });
}

function sendTheGameData() {
    getRequestAttractions(funcToSendGame);
}

function postRequestGame(data,attr_id,game_kind){
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/'+
        attr_id+'/'+game_kind+'/',
        JSON.stringify(data));
}