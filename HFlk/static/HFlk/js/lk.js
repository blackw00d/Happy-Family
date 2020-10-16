const fadeTime = 300;

$(document).ready(function () {
    recalculateTotalCart();

    $("#sidebarnav li").click(function () {
        $('.active').removeClass();
        this.className = 'active';
    });
    $("#settingsclick").click(function () {
        let top = document.getElementById('controlpanel');
        top.className = '';
        top.style = 'display:none;'
        top = document.getElementById('settings');
        top.className = 'page-wrapper';
        top.style = 'visibility: visible;position:absolute;top:70px;height:calc(100% - 70px);width:85%';
        top = document.getElementById('orders');
        top.className = '';
        top.style = 'display:none';
    });
    $("#panelclick").click(function () {
        let top = document.getElementById('settings');
        top.className = '';
        top.style = 'display:none;position:absolute;top:70px;height:70%;';
        top = document.getElementById('controlpanel');
        top.className = 'page-wrapper';
        top.style = 'visibility: visible;';
        top = document.getElementById('orders');
        top.className = '';
        top.style = 'display:none;';
    });
    $("#ordersclick").click(function () {
        let top = document.getElementById('settings');
        top.className = '';
        top.style = 'display:none;position:absolute;top:70px;height:70%;';
        top = document.getElementById('controlpanel');
        top.className = '';
        top.style = 'display:none;position:absolute;top:70px;height:70%;';
        top = document.getElementById('orders');
        top.className = 'page-wrapper';
        top.style = 'visibility: visible;position:absolute;top:70px;width:85%;';
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