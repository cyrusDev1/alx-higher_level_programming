$('document').ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const code = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + code;
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
