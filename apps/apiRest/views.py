from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

from apps.petshop.models import Producto

# Create your views here.

class ObtenerProductos(View):
    def get(self,request):
        productos = Producto.objects.all()
        return JsonResponse(list(productos.values()), safe=False)


 