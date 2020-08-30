const fadeTime = 300;

$(document).ready(function () {
    recalculateCart();

    $("#sidebarnav li").click(function (e) {
        var top = document.getElementsByClassName('active');
        for (var i in top) {
            top[i].className = '';
        }
        this.className = 'active';
    });
    $("#settingsclick").click(function (e) {
        var top = document.getElementById('controlpanel');
        top.className = '';
        top.style = 'display:none;'
        var top = document.getElementById('settings');
        top.className = 'page-wrapper';
        top.style = 'visibility: visible;position:absolute;top:70px;height:calc(100% - 70px);width:85%';
        var top = document.getElementById('orders');
        top.className = '';
        top.style = 'display:none';
    });
    $("#panelclick").click(function (e) {
        console.log(1);
        var top = document.getElementById('settings');
        top.className = '';
        top.style = 'display:none;position:absolute;top:70px;height:70%;';
        var top = document.getElementById('controlpanel');
        top.className = 'page-wrapper';
        top.style = 'visibility: visible;';
        var top = document.getElementById('orders');
        top.className = '';
        top.style = 'display:none;';
    });
    $("#ordersclick").click(function (e) {
        var top = document.getElementById('settings');
        top.className = '';
        top.style = 'display:none;position:absolute;top:70px;height:70%;';
        var top = document.getElementById('controlpanel');
        top.className = '';
        top.style = 'display:none;position:absolute;top:70px;height:70%;';
        var top = document.getElementById('orders');
        top.className = 'page-wrapper';
        top.style = 'visibility: visible;position:absolute;top:70px;height:calc(100% - 70px);width:85%';
    });
});

function recalculateCart() {

    $('.shopping-cart').each(function () {
        var total = 0;
        $(this).find('.product').each(function () {
            total += parseFloat($(this).children('.product-price').text());
        });

        $(this).find('.totals-value').fadeOut(fadeTime, function () {
            $(this).closest('#cart-total').html(total.toFixed(2) + " &#x20BD;");
            $('.totals-value').fadeIn(fadeTime);
        });
    });
}