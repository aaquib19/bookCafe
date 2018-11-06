 $(document).ready(function () {

    $(window).on('scroll', function () {
        if ($(window).scrollTop() >= 10) { // use any value lower than the navbar height, [20] is an example

            $('.navbar').css({ // reducing the vertical padding from 25px to 10px
                'padding-top': '10px',
                'padding-bottom': '10px',
                'background': '#7386d5',
                'color': 'black',


            });

        } else {

            $('.navbar').css({ // reset the vertical padding to its initial value [25px]
                'padding-top': '25px',
                'padding-bottom': '25px',
                'background':'transparent',
                
            });

        }
    });

});
