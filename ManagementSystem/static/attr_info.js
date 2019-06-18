let arrOfPicsData = [];

window.onload = function () {
    let submitBTN = document.getElementById("submit_btn_add_attr");
    submitBTN.addEventListener('click', function () {
        sendTheAttractionWithAllInformation();
    });

    let desc = document.getElementById("desc");
    let desc_english = document.getElementById("desc_english");

    let hebrewBTN = document.getElementById("hebrewBTN");
    let englishBTN = document.getElementById("englishBTN");

    hebrewBTN.addEventListener('click', function () {
        desc.style.display = "";
        desc_english.style.display = "none";
    });

    englishBTN.addEventListener('click', function () {
        desc.style.display = "none";
        desc_english.style.display = "";
    });
    initializeTheListOfPicturesToShow();
};

function initializeTheListOfPicturesToShow() {
    //Check File API support
    if (window.File && window.FileList && window.FileReader) {
        var filesInput = document.getElementById("files");

        filesInput.addEventListener("change", function (event) {

            var files = event.target.files; //FileList object
            var output = document.getElementById("result");

            for (var i = 0; i < files.length; i++) {
                var file = files[i];

                //Only pics
                if (!file.type.match('image'))
                    continue;

                var picReader = new FileReader();

                picReader.addEventListener("load", function (event) {

                    var picFile = event.target;

                    var div = document.createElement("div");

                    div.innerHTML = "<img class='thumbnail' src='" + picFile.result + "'" +
                        "title='" + picFile.name + "'/>";

                    let picURL = picFile.result;
                    arrOfPicsData.push(picURL);
                    output.insertBefore(div, null);

                });

                //Read the image
                picReader.readAsDataURL(file);
            }

        });
    } else {
        console.log("Your browser does not support File API");
    }
}

function sendTheAttractionWithAllInformation() {
    let namee = localStorage.getItem("name_for_add_aq");
    let xx = JSON.parse(localStorage.getItem("x"));
    let yy = JSON.parse(localStorage.getItem("y"));
    let vidArr = 'hello';
    let pixArr = 'null';
    if (arrOfPicsData.length > 0) {
        pixArr = "hello";
        // can do it with all pics.. just add loop
        sendLongBase64PartsPic(arrOfPicsData[0]);
        window.location.href = '/add_game';
    }
    let attraction_to_send = {
        name: namee
        , x: xx, y: yy
        , description: document.getElementById("desc").value + ";;" + document.getElementById("desc_english").value
        //, script: JSON.parse(localStorage.getItem("script"))
        , picturesURLS: pixArr, videosURLS: vidArr
    };
    postRequestAttractionSync(attraction_to_send);
    localStorage.setItem("name_for_add_aq", attraction_to_send.name);
    localStorage.setItem("desc_for_add_aq", attraction_to_send.description);
    window.location.href = '/add_game';
}


function postRequestAttractionSync(attraction) {
    syncServerRequest("POST", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/attraction/',
        JSON.stringify(attraction));
}

