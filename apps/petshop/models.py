from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


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
    # stock = models.IntegerField() 
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    id_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagen_url = models.ImageField(upload_to='imagenesProducto')

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