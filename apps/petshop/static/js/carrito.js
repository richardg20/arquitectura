document.addEventListener('DOMContentLoaded', function() {
  var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

  var agregarCarritoButtons = document.getElementsByClassName('agregar-carrito');

  Array.prototype.forEach.call(agregarCarritoButtons, function(button) {
    button.addEventListener('click', function(event) {
      event.preventDefault();
      var sku = this.getAttribute('data-sku');
      cartItems.push(sku);
      localStorage.setItem('cartItems', JSON.stringify(cartItems));
    });
  });

 
});


//Guardar datos del GymUser
document.getElementById("guardar").addEventListener("click", function () {
  // Obtener los nuevos valores de los campos
  var nombre = document.getElementById("nombre").value;
  var email = document.getElementById("email").value;
  var edad = document.getElementById("edad").value;
  var objetivo = document.getElementById("objetivo").value;
  var peso = document.getElementById("peso").value;
  var altura = document.getElementById("altura").value;

  // Realizar una solicitud Ajax para actualizar los datos en Django
  // Aquí debes proporcionar la URL y la vista adecuada en Django para manejar la actualización de datos.

  // Actualizar la zona "GymUser" con los nuevos datos
  document.getElementById("username").textContent = nombre;
});







