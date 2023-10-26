from django.shortcuts import render, redirect
from .models import *
import os
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Producto
from django.core import serializers
from collections import Counter
from collections import defaultdict
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import json
#from .forms import UserProfileForm
# Create your views here.

def  cargarInicio(request):
    return render(request,'inicio.html')


def  cargarDescripcion(request):
    return render(request,'descripcion.html')


def  cargarCatalogo(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,"catalogo.html",{"cate":categorias, "prod":productos})

def muestraCat(request):
    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtNombre']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    v_descripcion = request.POST['txtDescripcion']
    v_img = request.FILES['txtImg']
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    Producto.objects.create(sku = v_sku,nombre = v_nombre,stock = v_stock,precio = v_precio,descripcion = v_descripcion, id_categoria = v_categoria, imagen_url = v_img)        

    return redirect('/catalogo')

def  cargarEditar(request):
    return render(request,'editar.html')


def cargarLogin(request):
    return render(request,'login.html')

def cargarSignup(request):
    return render(request,'signup.html')

def cargarCarro(request):
    return render(request,'carro.html')

def cargarAgregarProducto(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,"agregar.html",{"cate":categorias, "prod":productos})

def agregarProducto(request):

    v_sku = request.POST['txtSku']

    v_nombre = request.POST['txtNombre']
    #v_stock = request.POST['txtStock']
    v_stock = 0
    v_precio = request.POST['txtPrecio']
    v_descripcion = request.POST['txtDescripcion']
    v_img = request.FILES['txtImg']
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])


    #Producto.objects.create(nombre = v_nombre, precio = v_precio,descripcion = v_descripcion,imagen_url = v_img)  

    producto = Producto(
        sku= v_sku,
        nombre= v_nombre,
        stock = v_stock,
        precio = v_precio,
        descripcion = v_descripcion,
        id_categoria = v_categoria,
        imagen_url = v_img,
    )

    producto.save()
    messages.success(request,'Objeto ingresado correctamente')
    return redirect('/agregar')

    try:
        if(int(v_sku) == Producto.objects.get(sku = v_sku).sku ):
            messages.error(request,'El objeto que intenta agregar ya existe')
            return   redirect('/agregar')
             
    except ObjectDoesNotExist:
            # Producto.objects.create(sku = v_sku,nombre = v_nombre,stock = v_stock,precio = v_precio,descripcion = v_descripcion, id_categoria = v_categoria, imagen_url = v_img)
            Producto.objects.create(nombre = v_nombre, precio = v_precio,descripcion = v_descripcion,imagen_url = v_img)  
            messages.success(request,'Objeto ingresado correctamente')
            return redirect('/agregar')
    



def cargarEditarProducto(request,sku):
    productos = Producto.objects.get(sku = sku)
    categorias = Categoria.objects.all()
    return render(request,"editar.html",{"prod":productos,"cate":categorias})

def editarProducto(request):
    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(sku = v_sku)
    v_nombre = request.POST['txtNombre']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    v_descripcion = request.POST['txtDescripcion']
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    try:
        v_img = request.FILES['txtImg']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.imagen_url))
        os.remove(ruta_imagen)
    except:
        v_img = productoBD.imagen_url


    productoBD.nombre = v_nombre
    productoBD.stock = v_stock
    productoBD.precio = v_precio
    productoBD.descripcion = v_descripcion
    productoBD.imagen_url = v_img
    productoBD.id_categoria = v_categoria

    productoBD.save()


    return redirect('/agregar')


def eliminarProducto(request,sku):
    producto = Producto.objects.get(sku = sku)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.imagen_url))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('/agregar')


def carrito(request):
    
    return HttpResponse("Ok")

def loguearse(request):
    if request.method == 'GET':
        return render(request, 'login.html',{
        'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'login.html',{
                'form': AuthenticationForm,
                'error': 'Usario o contrasenia incorrectos'
            })
        else:
            login(request, user)
            return redirect('/inicio')

def obtener_productos(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        skus = data.get('skus', [])

        sku_counter = defaultdict(int)  

        for sku in skus:
            sku_counter[sku] += 1  

        sku_list = list(set(skus)) 

        productos = Producto.objects.filter(sku__in=sku_list)

        response_data = []
        for producto in productos:
            sku = producto.sku
            cantidad = sku_counter[sku] 
            categoria = producto.id_categoria
            response_data.append({
                #'sku': producto.sku,
                'nombre': producto.nombre,
                #'imagen_url': producto.imagen_url.url,
                #'stock': producto.stock,
                'precio': producto.precio,
                'descripcion': producto.descripcion,
                #'id_categoria': categoria.id_categoria,
                #'nombre_categoria': categoria.nombre_categoria,
                #'cantidad': cantidad 
            })

        return JsonResponse(response_data, safe=False)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def actualizar_stock(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sku = data.get('sku')
        cantidad = data.get('cantidad')
        print("111111111",cantidad)
        print("222222222",sku)
        if sku is not None and cantidad is not None:
            try:
                producto = Producto.objects.get(sku=sku)
                if(cantidad>producto.stock):
                    cantidad = producto.stock
                    producto.stock -= int(cantidad) 
                    producto.save()  
                else:
                    producto.stock -= int(cantidad)  
                    print("33333333",cantidad)
                    producto.save()  
                    return JsonResponse({'status': 'ok'})
            except Producto.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Producto no encontrado'})
            except ValueError:
                return JsonResponse({'status': 'error', 'message': 'Cantidad inválida'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Falta SKU o cantidad'})

    return JsonResponse({'status': 'error', 'message': 'Request invalido'})





def registrarse(request):

    if request.method == 'GET':
        return render(request,"signup.html",{
        'form': UserCreationForm
        })
    else:
        if request.POST['contrasenia_i'] == request.POST['contrasenia_f']:
            
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['contrasenia_i'])
                print(user)
                user.save()
                login(request, user) 
                return redirect('/inicio')
            except:
                return render(request,"signup.html",{
                    'form': UserCreationForm,
                    "error": 'Este usuario ya existe'
                })   
        return render(request,"signup.html",{
            'form': UserCreationForm,
            "error": 'Las contrasenias ingresadas deben ser iguales'
        })  


def log_out(request):
    logout(request)
    return redirect('/inicio')


# def completar_rutina():
#         completar_
    
    
#     return redirect('/inicio')

#Funciones perfil de usuario
def actualizar_perfil(request):
    if request.method == 'POST':
        # Obtén los datos del formulario y realiza la actualización en la base de datos
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        edad = request.POST.get('edad')
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        objetivo = request.POST.get('objetivo')
        form = UserProfileForm(request.POST)
        
        if form.is_valid():
            # Guarda los datos actualizados en la base de datos
            form.save()
            return redirect('perfil')
    else:
        form = UserProfileForm()
        # Actualiza los datos en la base de datos aquí

        # Devuelve una respuesta JSON
        return JsonResponse({'success': True, 'nombre': nombre, 'email': email, 'edad': edad, 'peso': peso, 'altura': altura, 'objetivo': objetivo})

    return render(request, 'perfil.html')

