$('footer').hide();
$(window).scroll(function() {
    if ($(this).scrollTop() < 600) {
        $('footer').hide();
    }
    else {
        $('footer').show();
    }
});
