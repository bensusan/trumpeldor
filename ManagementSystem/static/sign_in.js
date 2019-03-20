function checkPassword() {
    var username=document.getElementById("user_name").value;
    var password=document.getElementById("password").value;
        if(username=="admin"&& password=="1234") {
            window.location.href = "/main";
        }
        else
           document.getElementById("errorMsg").innerHTML = "wrong password or username!";
}


// let points = [{lat: 31.263465932844372, lng: 34.801946282386783}];
let points = [];
let short = [];
let medium = [];
let long = [];
localStorage.setItem("points",JSON.stringify(points));
localStorage.setItem("short_path",JSON.stringify(short));
localStorage.setItem("medium_path",JSON.stringify(medium));
localStorage.setItem("long_path",JSON.stringify(long));

let shortPaths=[[]];
localStorage.setItem("short_paths",JSON.stringify(shortPaths));

//
// let short= [{lat: 31.263465932844372, lng: 34.801946282386783}];
//
// let med= [
//     {lat: 31.263465932844372, lng: 34.801946282386783},
//     {lat: 31.263065932844372, lng: 34.801146282386783}
// ];
//
// let long= [
//     {lat: 31.263465932844372, lng: 34.801946282386783},
//     {lat: 31.263065932844372, lng: 34.801146282386783},
//     {lat: 31.263865932844372, lng: 34.802146282386783}
// ];


// localStorage.setItem("numberOfPoints",""+points.length);

// localStorage.setItem("medium_path",JSON.stringify(med));
// localStorage.setItem("long_path",JSON.stringify(long));