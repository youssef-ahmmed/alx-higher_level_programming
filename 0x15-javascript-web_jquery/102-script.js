$(document).ready(() => {
  $('#btn_translate').click(() => {
    const language_code = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/', {lang: language_code}, (data) => {
      $('#hello').html(data.hello);
    });
  });
});
