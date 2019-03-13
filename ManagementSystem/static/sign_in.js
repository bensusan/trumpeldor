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

//
// let points= [
//     {lat: 31.263465932844372, lng: 34.801946282386783},
//     {lat: 31.263065932844372, lng: 34.801146282386783},
//     {lat: 31.263865932844372, lng: 34.802146282386783},
//     {lat: 31.262773527283052, lng: 34.802075028419495}
// ];

let points = [{lat: 31.263465932844372, lng: 34.801946282386783}];

let short= [
    {lat: 31.263465932844372, lng: 34.801946282386783}
];

let med= [
    {lat: 31.263465932844372, lng: 34.801946282386783},
    {lat: 31.263065932844372, lng: 34.801146282386783}
];

let long= [
    {lat: 31.263465932844372, lng: 34.801946282386783},
    {lat: 31.263065932844372, lng: 34.801146282386783},
    {lat: 31.263865932844372, lng: 34.802146282386783}
];

localStorage.setItem("points",JSON.stringify(points));
// localStorage.setItem("numberOfPoints",""+points.length);

localStorage.setItem("short_path",JSON.stringify(short));
localStorage.setItem("medium_path",JSON.stringify(med));
localStorage.setItem("long_path",JSON.stringify(long));

// alert("the number of points is now :" + points.length)

var shortPaths=[[]];

localStorage.setItem("short_paths",JSON.stringify(shortPaths));
// localStorage.setItem("medium_path",JSON.stringify(med));
// localStorage.setItem("long_path",JSON.stringify(long));