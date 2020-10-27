$(document).ready(function () {

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