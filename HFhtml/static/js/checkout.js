const fadeTime = 300;

$(document).ready(function () {
    recalculateCart();
    $('input[name="selector"][value="online"]').prop('checked', true);
});

$(document).delegate(".remove-product", "click", function (e) {
    e.preventDefault();
    removeItem(this);

    const basketcounter = parseInt($('#basketbtn span').text());
    const data = {};
    data['csrfmiddlewaretoken'] = $('.shopping-cart [name="csrfmiddlewaretoken"]').val();
    data['name'] = $(this).data('name');

    const url = '../BasketRemove/';
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
        success: function () {
            $('#basketbtn span').text((basketcounter - 1).toString());
            recalculateCart();
        }
    })
});

function recalculateCart() {
    let total = 0;

    $('.product').each(function () {
        total += parseFloat($(this).children('.product-price').text());
    });

    /* Update totals display */
    $('.totals-value').fadeOut(fadeTime, function () {
        $('#cart-total').html(total.toFixed(2) + " &#x20BD;");
        if (total === 0) {
            $('.checkout').fadeOut(fadeTime);
            $('.shopping-cart').html("<h1>Ваша корзина пуста</h1>\n" +
                "<h0>Корзина ждет, что ее наполнят. Желаем приятных покупок!</h0>");
        } else {
            $('.checkout').fadeIn(fadeTime);
        }
        $('.totals-value').fadeIn(fadeTime);
    });
}

/* Remove item from cart */
function removeItem(removeButton) {
    /* Remove row from DOM and recalculate cart total */
    const productRow = $(removeButton).parent().parent();
    productRow.remove();
    recalculateCart();
}