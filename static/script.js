function validateForm() {
  let x = document.forms["search"]["product"].value;
  if (x === "") {
    alert("Name must be filled out");
    return false;
  }
}