$(document).ready(() => {
  $('#add_item').click(function () {
    $('ul').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('ul.my_list li:last').remove();
  });
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
