document.addEventListener("DOMContentLoaded", function() {
  console.log('arquivo filtro_produtos.js carregado')

  const filterCodProd = document.querySelector("#filterCodprod");
  const filterNameProd = document.querySelector("#filterNameprod");

  function filterCard(){
    const codProdFilter = filterCodProd.value.trim().toLowerCase();
    const nameProdFilter = filterNameProd.value.trim().toLowerCase();
    const cards = document.querySelectorAll(".produtos-cadastrados .col-sm-2");

    cards.forEach((card) => {
      const codProd = card.querySelector("h3").textContent.toLowerCase();
      const nameProd = card.querySelector("p").textContent.toLowerCase();

      if (
        codProd.includes(codProdFilter) &&
        nameProd.includes(nameProdFilter)
      ) {
        card.style.display = "";
      } else {
        card.style.display = "none";
      }
    });
  }
  filterCodProd.addEventListener("input", filterCard);
  filterNameProd.addEventListener("input", filterCard);
});