$(document).ready(function(){
    
})
$(function(){
    $("#miFormulario").validate({
        rules:{
            txtNombre:{
                required:true,
                minlength:10
            },
            txtDescripcion:{
                required:true,
                minlength:10
            },
            txtValor:{
                required:true,
                minlength:5
            },
            txtStock:{
                required:true,
                minlength:1
            },
            txtImagen:{
                required:true,
                minlength:5
            }
        },
        messages:{
            txtNombre:{
                required: "Debe ingresar un nombre",
                minlength:"Debe ingresar al menos 10 caracteres"
            },
            txtDescripcion:{
                required: "Debe ingresar una descripcion",
                minlength:"Debe ingresar al menos 10 caracteres"
            },
            txtValor:{
                required: "Debe ingresar un valor",
                minlength:"Debe ingresar al menos 5 caracteres"
            },txtStock:{
                required: "Debe ingresar un stock",
                minlength:"Debe ingresar al menos 1 caracteres"
            },
            txtImagen:{
                required: "Debe ingresar la url de la imagen",
                minlength:"Debe ingresar al menos 5 caracteres"
            }

        }
    })
})