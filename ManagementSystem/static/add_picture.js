
var helperVar;

window.onload = function(){

initManyPicturesPresentation();
};

function initManyPicturesPresentation(){
    //Check File API support
    if(window.File && window.FileList && window.FileReader)
    {
        var filesInput = document.getElementById("files");

        filesInput.addEventListener("change", function(event){

            var files = event.target.files; //FileList object
            var output = document.getElementById("result");

            for(var i = 0; i< files.length; i++)
            {
                var file = files[i];

                //Only pics
                if(!file.type.match('image'))
                  continue;

                var picReader = new FileReader();

                picReader.addEventListener("load",function(event){

                    var picFile = event.target;

                    var div = document.createElement("div");

                    div.innerHTML = "<img class='thumbnail' src='" + picFile.result + "'" +
                            "title='" + picFile.name + "'/>";

                    output.insertBefore(div,null);

                });

                 //Read the image
                picReader.readAsDataURL(file);
            }

        });
    }
    else
    {
        console.log("Your browser does not support File API");
    }
}


function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
	image.src = URL.createObjectURL(element.files[0]);

    helperVar="";

  var file = element.files[0];
  var reader = new FileReader();
  reader.onloadend = function() {
   helperVar = reader.result
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
                let n_size = document.getElementById("n_size");
                let n_size_val = n_size.options[n_size.selectedIndex].value
                let data_send = {description: document.getElementById("game_instructions_text").value,
                    piecesURLS: helperVar, width: n_size_val, height: n_size_val};
                let attr_id = attr['id'];
                postRequestGame(data_send,attr_id,the_kind);
            }
             if(localStorage.getItem("game_kind")=="drag") {
                let the_kind = "puzzle";
                let n_size = document.getElementById("n_size").value;
                let data_send = {description: document.getElementById("game_instructions_text").value,
                    piecesURLS: helperVar, width: n_size, height: n_size};
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