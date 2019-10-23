function submitSellForm() {
    let name = document.getElementById('name-input').value;
    let description = document.getElementById('description-input').value;
    let price = document.getElementById('price-input').value;
    let image = document.getElementById('image').value;
    if (!name || !description || !price || !parseFloat(price) || !image) {
      return alert(`Some fields might be empty or incorrect. Please make ` + 
                   `sure that all the required fields have been completed ` + 
                   `correctly, and an image has been uploaded.`);
    }
    document.getElementById('name').value = name;
    document.getElementById('description').value = description;
    document.getElementById('price').value = price;
    document.getElementById('sell-form').submit();
  };

function payButtonClicked () {
    let address = document.getElementById('address_input').value;
    let city = document.getElementById('city_input').value;
    let email = document.getElementById('email_input').value;
    let mobile = document.getElementById('mobile_input').value;
  
    if (!address || !city || !email || !mobile) {
      return alert(`Some fields might be empty or incorrect. Please make ` +
                   `sure that all the required fields have been completed correctly.`);
    }
  
    var paymentForm = document.getElementById('payment-form');
  
    document.getElementById('address').value = address;
    document.getElementById('city').value = city;
    document.getElementById('email').value = email;
    document.getElementById('mobile').value = mobile;
  
    paymentForm.submit();
  }