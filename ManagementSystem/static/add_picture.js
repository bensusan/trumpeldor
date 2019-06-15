var helperVar;

window.onload = function () {
    let submitEverything = document.getElementById("submitEverything");
    submitEverything.addEventListener('click', function () {
        sendTheGameData();
    });

    let game_instructions_text = document.getElementById("game_instructions_text");
    let game_instructions_text_english = document.getElementById("game_instructions_text_english");
    let hebrewBTN = document.getElementById("hebrewBTN");
    let englishBTN = document.getElementById("englishBTN");

    hebrewBTN.addEventListener('click', function () {
        game_instructions_text.style.display = "";
        game_instructions_text_english.style.display = "none";

    });

    englishBTN.addEventListener('click', function () {
        game_instructions_text.style.display = "none";
        game_instructions_text_english.style.display = "";
    });
    initManyPicturesPresentation();
};

function initManyPicturesPresentation() {
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


function encodeImageFileAsURL(element) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(element.files[0]);

    helperVar = "";

    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        helperVar = reader.result;
        // alert(helperVar.length)
        // let comp = LZString.compress(helperVar)
        // alert(comp.length)
        // document.getElementById('game_instructions_text').value = helperVar;
        let len = helperVar.length / 10;
        let a = helperVar.substring(0, len);
        // let b = helperVar.substring(len,2*len);
        // let c = helperVar.substring(2*len,3*len);
        // let d = helperVar.substring(3*len,4*len);
        // let e = helperVar.substring(4*len,5*len);
        // let f = helperVar.substring(5*len,6*len);
        // let g = helperVar.substring(6*len,7*len);
        // let h = helperVar.substring(7*len,8*len);
        // let i = helperVar.substring(8*len,9*len);
        // let j = helperVar.substring(9*len,10*len);
        // document.getElementById('game_instructions_text').value = "" + _base64ToArrayBuffer(a) + "";
    }

    reader.readAsDataURL(file);
}




function _base64ToArrayBuffer(dataURI) {
    var BASE64_MARKER = ';base64,';

    var base64Index = dataURI.indexOf(BASE64_MARKER) + BASE64_MARKER.length;
    var base64 = dataURI.substring(base64Index);
    var raw = window.atob(base64);
    var rawLength = raw.length;
    var array = new Uint8Array(new ArrayBuffer(rawLength));

    for (i = 0; i < rawLength; i++) {
        array[i] = raw.charCodeAt(i);
    }
    return array;
}

function arrayBufferToBase64(buffer) {
    let binary = '';
    let bytes = new Uint8Array(buffer);
    let len = bytes.byteLength;
    for (let i = 0; i < len; i++) {
        binary += String.fromCharCode(bytes[i]);
    }
    return window.btoa(binary);
}

function funcToSendGame(attractionsJSON) {
    let name = localStorage.getItem("name_for_add_aq");
    let desc = localStorage.getItem("desc_for_add_aq");
    // alert("in get name! "+"of the origin : " + lat + " , " + lng);
    attractionsJSON.forEach(function (attr) {
        let p = {name: attr['name'], description: attr['description']};
        // alert("in get name! "+"of the origin : " + name + " , " + desc + "\n of the other: "+p.name +" , "+ p.description);
        if (p.name === name && p.description === desc) {
            let description = document.getElementById("game_instructions_text").value +
                ";;" + document.getElementById("game_instructions_text_english").value;


            if (localStorage.getItem("game_kind") == "sliding") {
                let the_kind = "sliding_puzzle";
                let n_size = document.getElementById("n_size");
                let n_size_val = n_size.options[n_size.selectedIndex].value;
                let data_send = {
                    description: description,
                    piecesURLS: helperVar, width: n_size_val, height: n_size_val
                };
                localStorage.setItem(name + the_kind, helperVar);
                let attr_id = attr['id'];
                postRequestGame(data_send, attr_id, the_kind);
            }
            if (localStorage.getItem("game_kind") == "drag") {
                let the_kind = "puzzle";
                let n_size = document.getElementById("n_size").value;
                let data_send = {
                    description: description,
                    piecesURLS: helperVar, width: n_size, height: n_size
                };
                localStorage.setItem(name + the_kind, helperVar);
                let attr_id = attr['id'];
                postRequestGame(data_send, attr_id, the_kind);
            }

            window.location.href = '/' + localStorage.getItem("last_add_game_url"); ////////////////////////////change to both
        }

    });
}

function sendTheGameData() {
    getRequestAttractions(funcToSendGame);
}

function postRequestGame(data, attr_id, game_kind) {
    serverRequest("POST", function noop(dummy) {
        }, 'http://' + ip + ':12344/managementsystem/attraction/' +
        attr_id + '/' + game_kind + '/',
        JSON.stringify(data));
}


var LZW = {
    compress: function (uncompressed) {
        "use strict";
        // Build the dictionary.
        var i,
            dictionary = {},
            c,
            wc,
            w = "",
            result = [],
            dictSize = 256;
        for (i = 0; i < 256; i += 1) {
            dictionary[String.fromCharCode(i)] = i;
        }

        for (i = 0; i < uncompressed.length; i += 1) {
            c = uncompressed.charAt(i);
            wc = w + c;
            //Do not use dictionary[wc] because javascript arrays
            //will return values for array['pop'], array['push'] etc
            // if (dictionary[wc]) {
            if (dictionary.hasOwnProperty(wc)) {
                w = wc;
            } else {
                result.push(dictionary[w]);
                // Add wc to the dictionary.
                dictionary[wc] = dictSize++;
                w = String(c);
            }
        }

        // Output the code for w.
        if (w !== "") {
            result.push(dictionary[w]);
        }
        return result;
    },


    decompress: function (compressed) {
        "use strict";
        // Build the dictionary.
        var i,
            dictionary = [],
            w,
            result,
            k,
            entry = "",
            dictSize = 256;
        for (i = 0; i < 256; i += 1) {
            dictionary[i] = String.fromCharCode(i);
        }

        w = String.fromCharCode(compressed[0]);
        result = w;
        for (i = 1; i < compressed.length; i += 1) {
            k = compressed[i];
            if (dictionary[k]) {
                entry = dictionary[k];
            } else {
                if (k === dictSize) {
                    entry = w + w.charAt(0);
                } else {
                    return null;
                }
            }

            result += entry;

            // Add w+entry[0] to the dictionary.
            dictionary[dictSize++] = w + entry.charAt(0);

            w = entry;
        }
        return result;
    }
}