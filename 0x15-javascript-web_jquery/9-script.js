$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (apiData) {
    $('div#hello').text(apiData?.hello);
  });
});
