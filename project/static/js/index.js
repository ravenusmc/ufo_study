//This function ensures that the user has entered the correct value at the login form.
function validateForm(){
    if (document.forms[0].username.value == "" || document.forms[0].password.value == "" ){
        alert('Please ensure you enter in both a username or password');
        return false;
    }
    return true;
}

//Code to calculate UFOs in a given state
$(function() {

    var submit_form = function(e) {
        //The /_by_state is the method that you will use.
      $.getJSON($SCRIPT_ROOT + '/_by_state', {
        //State_name is the name variable in the HTML code.
        state: $('input[name="state_name"]').val()
      }, function(data) {
        //This is where the data will be displayed.
        $('#state_results').text(data.result);
        // $('input[name=state_name]').focus().select();
      });
      return false;
    };

    //This is what will submit the form when the user clicks the link.
    $('a#state').bind('click', submit_form);
});


//Code to calculate UFO shapes
$(function() {

    var submit_form = function(e) {
        //The /_by_state is the method that you will use.
      $.getJSON($SCRIPT_ROOT + '/_by_shape', {
        //State_name is the name variable in the HTML code.
        shape: $('input[name="shape"]').val()
        //shape: $('select').val();
        // state: $s( "#shape option:selected" ).text();
      }, function(data) {
        //This is where the data will be displayed.
        $('#shape_results').text(data.result);
      });
      return false;
    };

    //This is what will submit the form when the user clicks the link.
    $('a#shape_button').bind('click', submit_form);
});


//Code to calculate UFO colors
$(function() {

    var submit_form = function(e) {
        //The /_by_state is the method that you will use.
      $.getJSON($SCRIPT_ROOT + '/_by_color', {
        //State_name is the name variable in the HTML code.
        color: $('input[name="color"]').val()
      }, function(data) {
        //This is where the data will be displayed.
        $('#color_results').text(data.result);
      });
      return false;
    };

    //This is what will submit the form when the user clicks the link.
    $('a#color_button').bind('click', submit_form);
});

//Code to calculate UFO's by state and shape
$(function() {

    var submit_form = function(e) {
        //The /_by_state is the method that you will use.
      $.getJSON($SCRIPT_ROOT + '/_by_state_shape', {
        state_two: $('input[name="state_two"]').val(),
        shape_two: $('input[name="shape_two"]').val()
      }, function(data) {
        //This is where the data will be displayed.
        $('#state_shape_results').text(data.result);
      });
      return false;
    };
    //This is what will submit the form when the user clicks the link.
    $('a#state_shape_btn').bind('click', submit_form);
});

//Code to calculate UFO's by year
$(function() {

    var submit_form = function(e) {
        //The /_by_state is the method that you will use.
      $.getJSON($SCRIPT_ROOT + '/_by_year', {
        year: $('input[name="year"]').val()
      }, function(data) {
        //This is where the data will be displayed.
        $('#year_results').text(data.result);
      });
      return false;
    };
    //This is what will submit the form when the user clicks the link.
    $('a#year').bind('click', submit_form);
});
