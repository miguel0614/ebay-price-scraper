function get_input(){
  // Get the input field
var input = document.getElementById("x1");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    //Final Actions
    let sub=document.getElementById('x1').value
    console.log(sub);
  }
});
}