$(() => {
  const newItem = $('<li></li>').text('Item');
  $('#add_item').click(() => {
    $('ul.my_list').append(newItem);
  });
});
