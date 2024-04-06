$('document').ready(function () {
  $('input#btn_translate').click(translate);
  $('input#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(apiUrl + $.param({ lang: $('INPUT#language_code').val() }), function (apiData) {
    $('div#hello').html(apiData.hello);
  });
}
