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
