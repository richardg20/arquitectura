const formulario = document.getElementById("formlogin");
document.addEventListener('DOMContentLoaded', function() {
    const formLogin = document.getElementById('formlogin');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    formLogin.addEventListener('submit', function(event) {
      if (usernameInput.value === '' || passwordInput.value === '') {
        event.preventDefault();
        showToast('Por favor, completa todos los campos.');
      }
      else{
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
  