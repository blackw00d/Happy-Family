const fadeTime = 300;

$(document).ready(function () {
    recalculateTotalCart();

    $("#sidebarnav li").click(function () {
        $('.active').removeClass();
        this.className = 'active';
    });
    $("#settingsclick").click(function () {
        $('#settings').addClass('page-wrapper').css({
            'position': 'absolute',
            'top': '70px',
            'width': '85%',
            'height': 'calc(100% - 70px)'
        }).show();
        $('#controlpanel').removeClass().hide();
        $('#orders').removeClass().hide();
    });
    $("#panelclick").click(function () {
        $('#settings').removeClass().hide().css({
            'position': 'absolute',
            'top': '70px',
            'height': '70%'
        });
        $('#controlpanel').addClass('page-wrapper').show();
        $('#orders').removeClass().hide();
    });
    $("#ordersclick").click(function () {
        $('#settings').removeClass().hide();
        $('#controlpanel').removeClass().hide();
        $('#orders').addClass('page-wrapper').css({
            'position': 'absolute',
            'top': '70px',
            'width': '85%'
        }).show();
    });
});

/* Displaying the total amount for each item */
function recalculateTotalCart() {
    $('.shopping-cart').each(function () {
        let total = 0;
        $(this).find('.product').each(function () {
            total += parseFloat($(this).children('.product-price').text());
        });

        $(this).find('.totals-value').fadeOut(fadeTime, function () {
            $(this).closest('#cart-total').html(total.toFixed(2) + " &#x20BD;");
            $('.totals-value').fadeIn(fadeTime);
        });
    });
}