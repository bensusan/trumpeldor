//menu_of_edit_attractions

document.getElementById("sideMenu").innerHTML = '<div class="sidenav">\n' +
    '  <h2 style="color:#818181;">עריכת אטרקציה</h2>' +
    '  <a href="/attractions">חזור</a>\n' +
    '  <button class="dropdown-btn">משחקים\n' +
    '    <i class="fa fa-caret-down"></i>\n' +
    '  </button>\n' +
    '  <div class="dropdown-container">\n' +
    '    <a id="add_game" href="/add_game_edit">הוספת משחק</a>\n' +
    '    <a href="/pick_delete_game">מחיקת משחק</a>\n' +
    '  </div>\n' +
    '  <a id="edit_aqs" href="/pick_aq_edit">עריכת שאלות אמריקאיות</a>\n' +
    '  <a id="edit_hints" href="/pick_hint_edit">עריכת רמזים</a>\n' +
     '  <a href="/main">לתפריט הראשי</a>\n' +
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


