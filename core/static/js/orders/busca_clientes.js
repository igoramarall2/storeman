document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("searchInput");
  const searchBtn = document.getElementById("searchBtn");
  const searchForm = document.getElementById("searchForm");
  const searchResults = document.getElementById("searchResults");
  const clientSelect = document.getElementById("clientSelect");

  // Iterate over the options
  for (var i = 0; i < clientSelect.options.length; i++) {
    var option = clientSelect.options[i];
    if (option.value != "") {
      console.log(option.value, option.textContent);
    }
  }
});
