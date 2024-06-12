$(document).ready(function() {
    $('#btn_translate').click(function() {
      const languageCode = $('#language_code').val();
      const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
      
      $.ajax({
        url: url,
        type: 'GET',
        success: function(response) {
          $('#hello').text(response.hello);
        },
        error: function(xhr, status, error) {
            console.log(`Error: ${error}`);
            console.log(`Status: ${status}`);
            console.log(xhr);
          $('#hello').text('Error fetching translation.');
        }
      });
    });
  });  