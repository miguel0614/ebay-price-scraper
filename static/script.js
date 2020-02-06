function validateForm() {
  let name = document.forms["search"]["product"].value;
  let priceLow = document.forms["search"]["price-min"].value;
  let priceHigh = document.forms["search"]["price-max"].value;
  if (name === "") {
    alert("Name must be filled out");
    return false;
  }
    if (priceLow !== '' && priceHigh !== ''){
      if (priceLow > priceHigh){
        alert("Price range must go from least to greater price");
        return false
      }
    }
  return true
}


