document.getElementById("sideMenu").innerHTML = '<div class="sidenav">\n' +
    '  <h2 style="color:#818181;">Welcome, Yael!</h2>' +
    '  <a href="/attractions">Manage Attractions</a>\n' +
    '  <button class="dropdown-btn">Paths\n' +
    '    <i class="fa fa-caret-down"></i>\n' +
    '  </button>\n' +
    '  <div class="dropdown-container">\n' +
    '  <button class="dropdown-btn">Add Path\n' +
    '    <i class="fa fa-caret-down"></i>\n' +
    '  </button>\n' +
    '  <div class="dropdown-container">\n' +
    '    <a href="maptrack">Short</a>\n' +
    '    <a href="maptrack">Medium</a>\n' +
    '    <a href="maptrack">Long</a>\n' +
    '  </div>\n' +
    '    <a href="#">Edit Path</a>\n' +
    '    <a href="#">Delete Path</a>\n' +
    '  </div>\n' +
    '  <a href="#services">Statistics</a>\n' +
    '  <a href="/additional_info">Additional Info</a>\n' +
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