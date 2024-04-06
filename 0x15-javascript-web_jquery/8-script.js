$.get('https://swapi.co/api/films/?format=json', function (apiData) {
  $('ul#list_movies').append(...apiData?.results?.map(movie => `<li>${movie?.title}</li>`));
});
