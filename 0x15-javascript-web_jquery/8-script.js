$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  const films = data.results;
  films.forEach(film => {
    $('#list_movies').append('<li>' + film.title + '</li>');
  });
});
