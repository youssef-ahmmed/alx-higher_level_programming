$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  $('#character').html(data.name);
});
