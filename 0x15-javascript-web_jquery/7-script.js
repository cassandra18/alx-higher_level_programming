$(document).ready(function(){
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        type: 'GET',
        success: function(response) {
            $('#character').text(response.name);
        },
        error: function() {
            $('#character').text('An error occurred while fetching the character');
        }
    });
    });