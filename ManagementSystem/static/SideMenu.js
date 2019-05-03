allowOnlyConnectedUsers();

document.getElementById("sideMenu").innerHTML = '<div class="sidenav">\n' +
    '  <h2 style="color:#818181;">!שלום, יעל</h2>' +
    '  <a href="/attractions" name="manage_attr_page">ניהול אטרקציות</a>\n' +
    '  <button class="dropdown-btn">מסלולים\n' +
    '    <i class="fa fa-caret-down"></i>\n' +
    '  </button>\n' +
    '  <div class="dropdown-container">\n' +
    '  <button class="dropdown-btn">הוספת מסלול\n' +
    '    <i class="fa fa-caret-down"></i>\n' +
    '  </button>\n' +
    '  <div class="dropdown-container">\n' +
    '    <a href="/add_short_path">קצר</a>\n' +
    '    <a href="/add_medium_path">בינוני</a>\n' +
    '    <a href="/add_long_path">ארוך</a>\n' +
    '  </div>\n' +
'  <button class="dropdown-btn">עריכת מסלול\n' +
    '    <i class="fa fa-caret-down"></i>\n' +
    '  </button>\n' +
    '  <div class="dropdown-container">\n' +
    '    <a href="/edit_short_path">קצר</a>\n' +
    '    <a href="/edit_medium_path">בינוני</a>\n' +
    '    <a href="/edit_long_path">ארוך</a>\n' +
    '  </div>\n' +
    '    <a href="/pick_path_delete">מחיקת מסלול</a>\n' +
    '  </div>\n' +
    '  <a href="#services">סטטיסטיקות</a>\n' +
    '  <a href="/additional_info">מידע נוסף</a>\n' +
    '  <button class="dropdown-btn">משוב\n' +
    '    <i class="fa fa-caret-down"></i>\n' +
    '  </button>\n' +
    '  <div class="dropdown-container">\n' +
    '    <a href="/feedback">הוסף משוב</a>\n' +
    '    <a href="/edit_feedbacks">מחק משוב</a>\n' +
    '  </div>\n' +
    '</div>\n' +
    '\n' +
    '<div class="main">\n' +
    '</div>';

/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
  this.classList.toggle("active");
  var dropdownContent = this.nextElementSibling;
  if (dropdownContent.style.display === "block") {
  dropdownContent.style.display = "none";
  } else {
  dropdownContent.style.display = "block";
  }
  });
}




// let points= [
//     {lat: 31.263465932844372, lng: 34.801946282386783},
//     {lat: 31.263065932844372, lng: 34.801146282386783},
//     {lat: 31.263865932844372, lng: 34.802146282386783},
//     {lat: 31.262773527283052, lng: 34.802075028419495}
// ];
//
// let short= [
//     {lat: 31.263465932844372, lng: 34.801946282386783}
// ];
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
//
// localStorage.setItem("points",JSON.stringify(points));
// localStorage.setItem("numberOfPoints",""+points.length);
//
// localStorage.setItem("short_path",JSON.stringify(short));
// localStorage.setItem("medium_path",JSON.stringify(med));
// localStorage.setItem("long_path",JSON.stringify(long));
//
// alert("the number of points is now :" + points.length)