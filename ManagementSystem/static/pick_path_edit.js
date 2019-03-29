
window.onload = function () {
    let path_length = document.getElementById("write_path_length");

    var editPathBTN = document.getElementById('edit_chosen_path');
    editPathBTN.addEventListener('click', function() {
        let length = path_length.value;
        if(length == "1"){
            window.location.href='/edit_short_path';
        }
        if(length == "2"){
            window.location.href='/edit_medium_path';
        }
        if(length == "3"){
            window.location.href='/edit_long_path';
        }
    });

};