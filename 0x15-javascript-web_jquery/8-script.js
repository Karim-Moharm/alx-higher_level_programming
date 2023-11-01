$(() => {
  $.ajax({
    type: 'Get',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    data: {
      format: 'json'
    },
    error: () => {
      console.error('error while fetching the data');
    },
    success: (data) => { // list_movies
      $.each(data.results, (idx, result) => {
        // $('#list_movies').append(`<li>${result.title}<li/>`);
        $('#list_movies').append(`${result.title} <br>`);
      });
    }
  });
});
