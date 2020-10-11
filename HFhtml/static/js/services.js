const fadeTime = 300;

/* Recalculate total for cart */
function recalculateCart(basket) {
    let total = 0;

    $('.product').each(function () {
        total += parseFloat($(this).children('.product-price').text());
    });

    /* Update totals display */
    $('.totals-value').fadeOut(fadeTime, function () {
        $('#cart-total').html(total.toFixed(2) + " &#x20BD;");
        if (total === 0) {
            $('.checkout').fadeOut(fadeTime);
            if (basket)
                $('.shopping-cart').html("<h1>Ваша корзина пуста</h1>\n" +
                    "<h0>Корзина ждет, что ее наполнят. Желаем приятных покупок!</h0>");
        } else {
            $('.checkout').fadeIn(fadeTime);
        }
        $('.totals-value').fadeIn(fadeTime);
    });
}


/* Ajax request to Django to remove item from basket session */
function basket_remove(){
    const basket_counter = parseInt($('#basketbtn span').text());
    const data = {};
    data['csrfmiddlewaretoken'] = $('.shopping-cart [name="csrfmiddlewaretoken"]').val();
    data['name'] = $(this).data('name');

    const url = 'BasketRemove/';
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
        success: function () {
            $('#basketbtn span').text((basket_counter - 1).toString());
            recalculateCart(false);
        }
    })
}

/* Remove item from cart */
function remove_item(removeButton) {
    /* Remove row from DOM and recalculate cart total */
    const productRow = $(removeButton).parent().parent();
    productRow.remove();
    recalculateCart();
}