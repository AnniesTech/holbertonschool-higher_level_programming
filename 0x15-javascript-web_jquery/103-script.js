const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      translate();
    }
  });
};

function translate () {
  const lan = $('INPUT#language_code').val();
  $.get('https://fourtonfish.com/hellosalut/?lang=' + lan, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
}
