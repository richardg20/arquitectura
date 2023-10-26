let valorM = false;
const formulario = document.getElementById("agregarProductoForm");
const toastContainer = document.getElementById("toastContainer"); 

// formulario.addEventListener('submit', function(evento){
//     evento.preventDefault();
    
//     var checkArray = [
//       { id: "txtSku", value: document.getElementById("txtSku").value },
//       { id: "txtPrecio", value: document.getElementById("txtPrecio").value },
//       { id: "txtNombre", value: document.getElementById("txtNombre").value },
//       { id: "txtImg", value: document.getElementById("txtImg").value },
//       { id: "txtDescripcion", value: document.getElementById("txtDescripcion").value },
//       { id: "txtStock", value: document.getElementById("txtStock").value },
//       { id: "cmbCategoria", value: document.getElementById("cmbCategoria").value }
//   ];
    
 

//   if (isNaN(parseInt(txtSku.value))) {
//     showToast("El SKU debe ser un número entero o esta incompleto.", txtSku.value);
//     return false;
//   }

 
//   else if (isNaN(parseInt(txtStock.value))) {
//     showToast("El stock debe ser un número entero o esta incompleto.");
//     return false;
//   }

  
//   else if (isNaN(parseInt(txtPrecio.value))) {
//     showToast("El precio debe ser un número entero o esta incompleto.");
//     return false;
//   }
//   else{

//     if (txtSku === "" || txtPrecio === "" || txtNombre === "" || txtDescripcion === "" || txtStock === "" || cmbCategoria.value === "Seleccione" || txtImg.files.length === 0 ) {
//       showToast("Falta uno o más campos por completar");
//       valorM = false;
//     } else{
       
//       valorM = true;
//       showModal();

//       var btnContinue = document.getElementById("btn-continue");

  
//       btnContinue.addEventListener("click", function(event) {
//         evento.preventDefault();
//         formulario.submit();
//       });
//     }
//   }
// });

function showToast(message, value) {
  const toastElement = document.createElement("div");
  toastElement.classList.add("toast");
  toastElement.setAttribute("role", "alert");
  toastElement.setAttribute("aria-live", "assertive");
  toastElement.setAttribute("aria-atomic", "true");

  const toastBody = document.createElement("div");
  toastBody.classList.add("toast-body");
  toastBody.innerHTML = message;

  const toastValue = document.createElement("div");
  toastValue.classList.add("toast-value");
  toastValue.innerHTML = value || "";

  toastElement.appendChild(toastBody);
  toastElement.appendChild(toastValue);

  toastContainer.appendChild(toastElement); 

  const bootstrapToast = new bootstrap.Toast(toastElement);
  bootstrapToast.show();
}


function showModal() {
    var modalSuccess = document.getElementById("modalSuccess");
    if (valorM === true) {
      var modal = new bootstrap.Modal(modalSuccess);
      modal.show();
      valorM = false;
    } else {
      modalSuccess.classList.remove("modalSuccess");
    }
  }




 function crearStorage(){
  let array = [];
  localStorage.setItem("myStorage", JSON.stringify(array));
}

function obtenerStorage(){
  return JSON.parse(localStorage.getItem("myStorage"));
}

function guardarStorage(array){
  localStorage.setItem("myStorage", JSON.stringify(array));
}



