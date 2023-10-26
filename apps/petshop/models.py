from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django import forms
from django.db import models


# Create your models here.
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        txt = "Nombre: {0} - Id: {1}"
        return txt.format(self.nombre_categoria,self.id_categoria)

class Producto(models.Model):
    #sku = models.IntegerField(primary_key=True)
    sku = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=1500)
    stock = models.IntegerField(null=True, default=0) 
    precio = models.IntegerField(null=True, default=0)
    #precio = models.IntegerField()
    descripcion = models.CharField(max_length=1000)
    id_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagen_url = models.ImageField(upload_to='imagenesProducto', null=True)

    def __str__(self):
        txt = "N° {0} - Stock: {1} - nombre: {2}"
        return txt.format(self.sku,self.stock, self.nombre)




class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True, default="id")
    nombre = models.CharField(max_length=50, default="usuario")   
    contraseña = models.CharField(max_length=100, default="password")
    rutina_completa = models.IntegerField(default=0)
    def __str__(self):
        txt = "ID: {0} - Nombre: {1} "
        return txt.format(self.idusuario, self.nombre)
    
    
#Clases de Perfil de usuario
class UserProfile(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    edad = models.EmailField(max_length=2)
    peso = models.EmailField(max_length=3)
    altura = models.EmailField(max_length=3)
    objetivo = models.EmailField(max_length=200)
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nombre', 'email', 'edad', 'peso', 'altura', 'objetivo']