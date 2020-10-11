import './services'

$(document).ready(function () {
    recalculateCart(false);
});

/* Remove item from basket when click on .remove-product */
$(document).delegate(".remove-product", "click", function (e) {
    e.preventDefault();
    remove_item(this);
    basket_remove();
});