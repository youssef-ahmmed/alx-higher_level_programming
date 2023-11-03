$(document).ready(() => {
  $('#btn_translate').click(parse);
  $('#language_code').keyup((e) => {
    if (e.keyCode === 13) {
      parse();
    }
  });
});

function parse () {
  const language_code = $('#language_code').val();
  $.get('https://hellosalut.stefanbohacek.dev/', {lang: language_code}, (data) => {
    $('#hello').html(data.hello);
  });
}
