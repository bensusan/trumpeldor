var cuisines = ["Chinese","Indian"];

var sel = document.getElementById('CuisineList');
var fragment = document.createDocumentFragment();
cuisines.forEach(function(cuisine, index) {
    var opt = document.createElement('option');
    opt.innerHTML = cuisine;
    opt.value = cuisine;
    fragment.appendChild(opt);
});
sel.appendChild(fragment);