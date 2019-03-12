function checkPassword() {

    var username=document.getElementById("uname").value;
    var password=document.getElementById("psw").value;
        if(username=="admin"&& password=="1234")
            window.location.href = "/main";
        else
           document.getElementById("demo").innerHTML = "wrong password or username!";

}

function checkPassword1() {

    var fname=document.getElementById("fname").value;
    var lname=document.getElementById("lname").value
        if(fname=="admin"&& lname=="1234")
             window.location.href = "/main";
        else
           document.getElementById("demo").innerHTML = "wrong password or username!";

}

var shortPaths=[[]];

localStorage.setItem("short_paths",JSON.stringify(shortPaths));
// localStorage.setItem("medium_path",JSON.stringify(med));
// localStorage.setItem("long_path",JSON.stringify(long));