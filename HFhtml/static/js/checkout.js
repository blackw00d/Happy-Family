import './services'

$(document).ready(function () {
    recalculateCart(true);
    $('input[name="selector"][value="online"]').prop('checked', true);
});

/* Remove item from basket when click on .remove-product */
$(document).delegate(".remove-product", "click", function (e) {
    e.preventDefault();
    remove_item(this);
    basket_remove();
});