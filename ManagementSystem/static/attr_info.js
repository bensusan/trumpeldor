var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};

let arrOfPicsData = [];

window.onload = function(){

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

                    let picURL = picFile.result;
                    arrOfPicsData.push(picURL);
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
};


    function sendAll() {
        alert("sda2231");
        let name = JSON.parse(localStorage.getItem("nameo"));
        let x = JSON.parse(localStorage.getItem("x"));
        let y = JSON.parse(localStorage.getItem("y"));
        alert(name);
        // let vidArr = JSON.parse(localStorage.getItem("vidArr"));
        // alert("is what: "+ addedPoint.lat +", " + addedPoint.lng + ", "+ (typeof addedPoint.lng));
        // alert("2!");
        // currPoints.push(addedPoint);


        let attraction_to_send = {
            name:name
            //,x:31.262860,y:34.801753
            ,x:x ,y:y
            ,description:document.getElementById("desc").value
            ,picturesURLS:[] ,videosURLS:[]};
        postRequestAttractionn(attraction_to_send);
        localStorage.setItem("name_for_add_aq", attraction_to_send.name);
        localStorage.setItem("desc_for_add_aq", attraction_to_send.description);
        window.location.href='/add_game';
        // window.location.href='/attractions';
        // alert("point:"+localStorage.getItem("addedPoint")+"\n"+
        //     "name:"+document.getElementById("attr_name").value);
    }


    function postRequestAttractionn(attraction){
    serverRequest("POST", function noop(dummy){}, 'http://'+ip+':12344/managementsystem/attraction/',
        JSON.stringify(attraction));
}