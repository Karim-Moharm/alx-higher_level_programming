$(() => {
  $.ajax({
    type: 'Get',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    data: {
      format: 'json'
    },
    error: () => {
      console.error('error while fetching the data');
    },
    success: (data) => {
      $('#character').append(data.name);
    }
  });
});
