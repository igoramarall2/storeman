document.addEventListener("DOMContentLoaded", function () {
  // FILTRO DE PRODUTOS
  const filterCodProd = document.querySelector("#filterCodprod");
  const filterNameProd = document.querySelector("#filterNameprod");
  const rows = document.querySelectorAll("#productTable tbody tr");

  function filterRows() {
    const codProdFilter = filterCodProd.value.trim().toLowerCase();
    const nameProdFilter = filterNameProd.value.trim().toLowerCase();

    rows.forEach((row) => {
      const codProd = row
        .querySelector("td:nth-child(3)")
        .textContent.toLowerCase();
      const nameProd = row
        .querySelector("td:nth-child(4)")
        .textContent.toLowerCase();

      if (
        codProd.includes(codProdFilter) &&
        nameProd.includes(nameProdFilter)
      ) {
        row.style.display = "";
      } else {
        row.style.display = "none";
      }
    });
  }
  filterCodProd.addEventListener("input", filterRows);
  filterNameProd.addEventListener("input", filterRows);
});