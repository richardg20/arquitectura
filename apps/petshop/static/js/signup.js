const formulario = document.getElementById("register");

document.addEventListener('DOMContentLoaded', function() {
  const formRegister = document.getElementById('register');
  const usernameInput = document.getElementById('username');
  const passwordInput = document.getElementById('contrasenia_i');
  const confirmPasswordInput = document.getElementById('contrasenia_f');
  formRegister.addEventListener('submit', function(event) {
    if (usernameInput.value === '' || passwordInput.value === '' || confirmPasswordInput.value === '') {
      event.preventDefault();
      showToast('Por favor, completa todos los campos.');
    } else if (passwordInput.value !== confirmPasswordInput.value) {
      event.preventDefault();
      showToast('Las contraseñas no coinciden.');
    } else {
      formulario.submit();
    }
  });

  function showToast(message) {
    const toastContainer = document.getElementById('toastContainer');
    const toastElement = document.createElement('div');
    toastElement.classList.add('toast');
    toastElement.setAttribute('role', 'alert');
    toastElement.setAttribute('aria-live', 'assertive');
    toastElement.setAttribute('aria-atomic', 'true');

    const toastBody = document.createElement('div');
    toastBody.classList.add('toast-body');
    toastBody.textContent = message;

    toastElement.appendChild(toastBody);
    toastContainer.appendChild(toastElement);

    const bootstrapToast = new bootstrap.Toast(toastElement);
    bootstrapToast.show();
  }
});
