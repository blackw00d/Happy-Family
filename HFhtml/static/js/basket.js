var fadeTime = 300;


$(document).ready(function () {
    recalculateCart();
});


$(document).delegate(".remove-product", "click", function (e) {
    e.preventDefault();
    removeItem(this);

    var basketcounter = parseInt($('#basketbtn span').text());
    var data = {}
    var crsf_token = $('.shopping-cart [name="csrfmiddlewaretoken"]').val();
    data['csrfmiddlewaretoken'] = crsf_token;
    data['name'] = $(this).data('name');

    var url = 'BasketRemove/'
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
    var total = 0;

    $('.product').each(function () {
        total += parseFloat($(this).children('.product-price').text());
    });

    /* Update totals display */
    $('.totals-value').fadeOut(fadeTime, function () {
        $('#cart-total').html(total.toFixed(2) + " &#x20BD;");
        if (total === 0) {
            $('.checkout').fadeOut(fadeTime);
        } else {
            $('.checkout').fadeIn(fadeTime);
        }
        $('.totals-value').fadeIn(fadeTime);
    });
}


/* Remove item from cart */
function removeItem(removeButton) {
    /* Remove row from DOM and recalc cart total */
    var productRow = $(removeButton).parent().parent();
    productRow.remove();
    recalculateCart();
}