$('document').ready(function () {
  $('INPUT#btn_translate').on('click', translate);
  $('INPUT#language_code').on('focus', function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const code = $('INPUT#language_code').val();
  const url = 'https://fourtonfish.com/hellosalut/?lang=' + code;
  $.get(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
}
