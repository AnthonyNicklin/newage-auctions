$(document).ready(function() {
    setInterval(function() {
        var docHeight = $(window).height();
        var footerHeight = $('#footer').height();
        var footerTop = $('#footer').position().top + footerHeight;
        var marginTop = (docHeight - footerTop + 10);

        if (footerTop < docHeight)
            $('#footer').css('margin-top', marginTop + 'px'); // padding of 30 on footer
        else
            $('#footer').css('margin-top', '0px');
    }, 250);
});