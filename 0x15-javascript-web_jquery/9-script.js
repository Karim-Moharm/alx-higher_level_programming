document.addEventListener("DOMContentLoaded", () => {
  $(() => {
    $.ajax({
      type: 'Get',
      url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
      data: {
        format: 'json'
      },
      error: () => {
        console.error('error while fetching the data');
      },
      success: (data) => {
        $('#hello').html(data.hello);
      }
    });
  });
});
