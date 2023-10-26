document.addEventListener('DOMContentLoaded', function() {
  var productosContainer = document.getElementById('productos-container');
  var storage = localStorage.getItem('cartItems');
  var skus = JSON.parse(storage);

  var skuCounters = {}; 
  var total = 0;
  var productData; 
  console.log(skus);
  if(skus===null){

  }
  else{
    skus.forEach(function(sku) {
      if (skuCounters[sku]) {
        skuCounters[sku] += 1;
      } else {
        skuCounters[sku] = 1; 
      }
    });
  
    console.table(skuCounters);
  
    fetch('/obtener-productos', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': token
      },
      body: JSON.stringify({ skus: skus })
    })
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        productData = data; 
  
        data.forEach(function(producto) {
          var sku = producto.sku;
          console.log("skuforeach datos",producto.sku);
          console.log("skuforeach datos 2",sku);
          var cantidad = skuCounters[sku] || 0;
  
          
          
          if(cantidad>producto.stock){
            cantidad = producto.stock;
            var subtotal = cantidad * producto.precio; 
            total += subtotal;
            var productoElement = document.createElement('tr');
          productoElement.innerHTML = `

            <td>${producto.nombre}</td>
            <td>${producto.descripcion}</td>

            <td><button class="eliminar-btn">Eliminar</button></td>
          `;
          producto.stock = 0;
          productosContainer.appendChild(productoElement);
          
          }
          else{
            var subtotal = cantidad * producto.precio; 
            total += subtotal;
            var productoElement = document.createElement('tr');
          productoElement.innerHTML = `

            <td>${producto.nombre}</td>
            <td>${producto.descripcion}</td>

 
            
          `;
          productosContainer.appendChild(productoElement);
          }
          
         
  
          var eliminarButton = productoElement.getElementsByClassName('eliminar-btn')[0];
         
  
  
        });
  
       
  
  
        var btnComprar = document.getElementById('btn-aumentar-rutina');
  
  
        btnComprar.addEventListener('click', function() {
  
          var firstProduct = productData[0]; 
          var sku = firstProduct.sku;
          var cantidad = skuCounters[sku] || 0;
  
          console.log("Restando cantidad:", cantidad); 
          for (var i = 0; i < data.length; i++) {
            var producto = data[i];
            console.log(producto)
            var sku = producto.sku;
            var cantidad = skuCounters[sku] || 0;
            actualizarStockEnBD(sku, cantidad);
         
   
          }
          event.preventDefault();
          cartItems = []; 
          localStorage.setItem('cartItems', JSON.stringify(cartItems));

        });
  
        
      })
      .catch(function(error) {
        console.log(error);
      });
  
    function crearEventoEliminar(producto, sku) {
      return function(event) {
        var productoElement = event.target.parentNode.parentNode;
        var cantidadElement = productoElement.getElementsByClassName('cantidad')[0];
  
  
        if (skuCounters[sku] > 0) {
          skuCounters[sku] -= 1;
          total -= producto.precio;

          var storage = localStorage.getItem('cartItems');
          var skus = JSON.parse(storage);
          console.log("sku antes de eliminar:", skus);
          var skuABuscarString = sku.toString();
          var index = skus.indexOf(skuABuscarString);
          console.log("Index antes de eliminar:", index); 
          if (index !== -1) {
            skus.splice(index, 1);
            localStorage.setItem('cartItems', JSON.stringify(skus));
            console.log("Array skus después de eliminar:", skus); 
            if (skuCounters[sku] === 0) {
              localStorage.setItem('cartItems', JSON.stringify(skus));
              console.log("LocalStorage actualizado:", localStorage.getItem('cartItems')); 
            }
          }
  
          if (skuCounters[sku] === 0) {
            productoElement.remove();
          }
        }
  
     
        console.log("skus después de eliminar:", skus);
        console.log("skuCounters después de eliminar:", skuCounters); 
      };
    }
  
    function actualizarStockEnBD(sku, cantidad) {
      fetch('/actualizar-stock', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': token
        },
        body: JSON.stringify({ sku: sku, cantidad: cantidad })
      })
        .then(function(response) {
    
          if (response.ok) {
            location.reload();
            console.log('Stock actualizado en la base de datos');
          } else {
          
            console.log('Error al actualizar el stock en la base de datos');
          }
        })
        .catch(function(error) {
        
          console.log('Error de conexión o procesamiento:', error);
        });
    }
  }
  
});






  