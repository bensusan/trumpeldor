//menu_of_edit_attractions

document.getElementById("sideMenu").innerHTML = '<div class="sidenav">\n' +
    '  <h2 style="color:#818181;">עריכת רמזים</h2>' +
    '  <a href="/main">לתפריט הראשי</a>\n' +
    '  <a href="/add_hint_edit">הוספת רמז</a>\n' +
    '  <a id="editHintBTNmenu">עריכת רמז</a>\n' +
    '  <a id="deleteHintBTNmenu">מחיקת רמז</a>\n' +
    '  <a href="/edit_attraction">!סיימתי</a>\n' +
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


