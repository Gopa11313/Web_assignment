
function validateUser(){
  var email = document.getElementById('login_email').value;
  var password=document.getElementById('login_password').value;

  if(email.indexOf('@')<=0){
    alert("invalid '@' position");
    return false;
  }

  if(password.length < 10){
      alert("Please enter more than 8 characters");
      return false;
  }
  alert("User has been added successfully !")

}


function validateCustomerEdit(){

  var firstname=document.getElementById('customerFname').value;
  var lastname=document.getElementById('customerLname').value;
  var email = document.getElementById('customerID').value;

  if (!isNaN(firstname)){
    alert("Only characters are allowed");
    return false;
  }
  if (!isNaN(lastname)){
      alert("Only characters are allowed");
      return false;
  }

  if(email.indexOf('@')<=0){
      alert("invalid '@' position");
      return false;
  }
  alert("Created successfully !")
}