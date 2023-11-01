$(() => {
  const headerClassColor = $('header').attr('class');
  $('#toggle_header').click(() => {
    if (headerClassColor === 'green') {
      $('header').toggleClass('red');
    }
    if (headerClassColor === 'red') {
      $('header').toggleClass('green');
    }
  });
});
