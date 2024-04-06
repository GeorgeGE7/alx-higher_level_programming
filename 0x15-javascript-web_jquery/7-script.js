$.get('https://swapi.co/api/people/5/?format=json', function (apiData) {
  $('DIV#character').text(apiData?.name);
});
