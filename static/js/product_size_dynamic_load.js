// static/js/admin_custom.js

document.addEventListener('DOMContentLoaded', function() {
    const productTypeSelect = document.querySelector('#id_product_type');

    productTypeSelect.addEventListener('change', function() {
        const productTypeId = this.value;
        fetch(`/api/ajax/get_sizes_for_product_type/${productTypeId}/`)
            .then(response => response.json())
            .then(data => {
                const sizeSelect = document.querySelector('#id_sizes');
                sizeSelect.innerHTML = ''; // Clear existing options
                data.forEach(size => {
                    const option = new Option(size.name, size.id, false, false);
                    sizeSelect.appendChild(option);
                });
            });
    });
});
