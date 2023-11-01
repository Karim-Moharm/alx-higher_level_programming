$(() => {
  const getHeaderClassColor = $('header').attr('class');
  $('#toggle_header').click(() => {
    if (getHeaderClassColor === 'green') {
      $('header').toggleClass('red');
    }
    if (getHeaderClassColor === 'red') {
      $('header').toggleClass('green');
    }
  });
});
