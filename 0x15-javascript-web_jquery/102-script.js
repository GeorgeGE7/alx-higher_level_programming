$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('input#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (apiData) {
      $('div#hello').html(apiData?.hello);
    });
  });
});
