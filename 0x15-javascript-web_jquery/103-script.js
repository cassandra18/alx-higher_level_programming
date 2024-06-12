$(document).ready(function() {
    function fetchHello() {
      const languageCode = $('#language_code').val();
      const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
  
      $.ajax({
        url: url,
        type: 'GET',
        success: function(response) {
          $('#hello').text(response.hello);
        },
        error: function(xhr, status, error) {
          console.error(`Error: ${error}`);
          console.error(`Status: ${status}`);
          console.error(xhr);
          $('#hello').text('Error fetching translation.');
        }
      });
    }
  
    $('#btn_translate').click(fetchHello);
  
    $('#language_code').keypress(function(event) {
      if (event.which === 13) { // Enter key pressed
        fetchHello();
      }
    });
  });
  