document.addEventListener("DOMContentLoaded", function () {
  // Get the CSRF token from the page
  const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  const productTable = document.getElementById("productTable");
  const selectedProductsTableBody = document.getElementById(
    "selectedProductsTableBody"
  );
  const totalPriceElement = document.getElementById("totalPrice");

  let totalPrice = 0;

  productTable.addEventListener("change", function (event) {
    if (event.target.classList.contains("selectCheckbox")) {
      const checkbox = event.target;
      const row = checkbox.closest("tr");

      if (checkbox.checked) {
        const clonedRow = row.cloneNode(true);
        const quantityInputCell = document.createElement("td"); // Novo <td> para conter o quantityInput
        const quantityInput = document.createElement("input");
        quantityInput.type = "number";
        quantityInput.value = 1; // Default quantity
        quantityInput.min = 1; // Minimum quantity allowed
        quantityInput.classList.add("quantityInput");
        quantityInput.classList.add("form-control");
        quantityInputCell.appendChild(quantityInput); // Adiciona o quantityInput ao novo <td>
        clonedRow.appendChild(quantityInputCell); // Adiciona o novo <td> à linha clonada

        // Adiciona a célula de valor antes da célula de quantidade
        const valueCell = clonedRow.querySelector("td:nth-child(6)");
        clonedRow.insertBefore(quantityInputCell, valueCell);

        selectedProductsTableBody.appendChild(clonedRow);

        const price = parseFloat(
          row.querySelector("td:nth-child(6)").textContent
        );
        const quantity = parseInt(quantityInput.value);
        const subtotal = price * quantity;
        totalPrice += subtotal;
      } else {
        const selectedRowIndex = [
          ...selectedProductsTableBody.children,
        ].findIndex((tr) => tr.dataset.id === row.dataset.id);
        if (selectedRowIndex !== -1) {
          const selectedRow =
            selectedProductsTableBody.children[selectedRowIndex];
          const price = parseFloat(
            selectedRow.querySelector("td:nth-child(7)").textContent
          );
          const quantity = parseInt(
            selectedRow.querySelector(".quantityInput").value
          );
          const subtotal = price * quantity;
          totalPrice -= subtotal;
          selectedRow.remove();

          // Uncheck the corresponding checkbox in the main table
          row.querySelector(".selectCheckbox").checked = false;
        }
      }

      updateTotalPrice();
    }
  });

selectedProductsTableBody.addEventListener("change", function (event) {
    if (event.target.classList.contains("quantityInput")) {
        // Update subtotal and total price if quantity changes
        const quantityInput = event.target;
        const row = quantityInput.closest("tr");
        const price = parseFloat(row.querySelector("td:nth-child(7)").textContent);
        const quantity = parseInt(quantityInput.value);
        const subtotal = price;
        row.querySelector("td:nth-child(7)").textContent = subtotal.toFixed(2);
        updateTotalPrice();
    } else if (event.target.classList.contains("selectCheckbox")) {
        // Handle checkbox changes
        const checkbox = event.target;
        const row = checkbox.closest("tr");

        if (!checkbox.checked) {
            // If checkbox is unchecked, remove corresponding row from selected products table
            const selectedRow = selectedProductsTableBody.querySelector(`tr[data-id="${row.dataset.id}"]`);
            if (selectedRow) {
                const price = parseFloat(selectedRow.querySelector("td:nth-child(7)").textContent);
                const quantity = parseInt(selectedRow.querySelector(".quantityInput").value);
                const subtotal = price * quantity;
                totalPrice -= subtotal;
                selectedRow.remove();
            }
            // Uncheck the corresponding checkbox in the main table
            const mainTableRow = productTable.querySelector(`tr[data-id="${row.dataset.id}"]`);
            if (mainTableRow) {
                mainTableRow.querySelector(".selectCheckbox").checked = false;
            }
        } else {
            // Check the corresponding checkbox in the main table
            const mainTableRow = productTable.querySelector(`tr[data-id="${row.dataset.id}"]`);
            if (mainTableRow) {
                mainTableRow.querySelector(".selectCheckbox").checked = true;
            }
        }
        updateTotalPrice(); // Update total price after any change
    }
});

  document
    .getElementById("queryProductsBtn")
    .addEventListener("click", function () {
      const selectedProductsArray = [];
      const selectedProductsTable = document.getElementById(
        "selectedProductsTableBody"
      );
      const checkboxes =
        selectedProductsTable.querySelectorAll(".selectCheckbox");

      checkboxes.forEach((checkbox) => {
        if (checkbox.checked) {
          const row = checkbox.closest("tr");
          const quantity = parseInt(row.querySelector(".quantityInput").value);
          selectedProductsArray.push({
            id: row.dataset.id,
            quantity: quantity,
          });
        }
      });
      const clientId = document.getElementById("clientSelect").value;

      console.log(selectedProductsArray);

      // Send the array to the server using AJAX
      $.ajax({
        type: "POST",
        url: "/saveorders/",
        headers: {
          "X-CSRFToken": csrfToken, // Function to get CSRF token from cookies
        },
        contentType: "application/json",
        data: JSON.stringify({
          produtos: selectedProductsArray,
          cliente: clientId,
        }),
        success: function (response) {
          console.log(response);
          // Handle the server response here
        },
        error: function (xhr, textStatus, errorThrown) {
          console.error("Error:", errorThrown);
        },
      });
    });

  function updateTotalPrice() {
    let totalPrice = 0;
    const selectedProductsTable = document.getElementById(
      "selectedProductsTableBody"
    );
    const rows = selectedProductsTable.querySelectorAll("tr");

    rows.forEach((row) => {
      const price = parseFloat(
        row.querySelector("td:nth-child(7)").textContent // Alterado para pegar a sétima célula (valor)
      );
      const quantity = parseInt(row.querySelector(".quantityInput").value);
      const subtotal = price * quantity;
      totalPrice += subtotal;
    });

    totalPriceElement.textContent = totalPrice.toFixed(2);
  }
});
