//menu_of_edit_attractions

document.getElementById("sideMenu").innerHTML = '<div class="sidenav">\n' +
    '  <h2 style="color:#818181;">Edit Attraction</h2>' +
    '  <a href="/attractions">Back</a>\n' +
    '  <a href="/add_game_edit">Add Game</a>\n' +
    '  <a href="/pick_aq_edit">Edit American Questions</a>\n' +
    '  <a href="/pick_hint_edit">Edit Hints</a>\n' +
     '  <a href="/main">Back to Main Page</a>\n' +
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


