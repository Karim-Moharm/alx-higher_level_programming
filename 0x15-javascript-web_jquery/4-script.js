$(() => {
    const getHeaderClassColor = $('header').attr('class');
    // console.log(getHeaderClassColor);
    $('#toggle_header').click(() => {
        if (getHeaderClassColor === 'green') {
            $('header').removeClass();
            $('header').toggleClass('red');
        }
        if (getHeaderClassColor === 'red') {
            $('header').removeClass();
            $('header').toggleClass('green');
        }
    });
});
