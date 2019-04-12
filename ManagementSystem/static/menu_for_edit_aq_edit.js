//menu_of_edit_attractions

document.getElementById("sideMenu").innerHTML = '<div class="sidenav">\n' +
     '  <h2 style="color:#818181;">עריכת שאלה אמריקאית</h2>' +
    '  <a href="/main">לתפריט הראשי</a>\n' +
    '  <a href="/add_aq">הוספת שאלה אמריקאית</a>\n' +
    '  <a id="want_to_edit_aq">עריכת שאלה אמריקאית</a>\n' +
    '  <a id="want_to_delete_aq">מחיקת שאלה אמריקאית</a>\n' +
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


