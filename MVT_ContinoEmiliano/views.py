
from django import http
from django.http import HttpResponse
from django.template import context, loader
from datetime import datetime
from app1.models import Familiar

def hola(request):
    return HttpResponse("<h1> HOLAAA! </h1>")

def mi_template(request):
    template = loader.get_template('mi_template.html')
    template_renderizado = template.render()
    return HttpResponse(template_renderizado)

def crear_familiar(request, nombre, apellido, edad):
    
    familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad, fecha_ingresado=datetime.now())
    familiar.save()
    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render({'familiar': familiar})
    
    return HttpResponse(template_renderizado)

def ver_familiares(request):
    
    familiares = Familiar.objects.all() #TRAE TODOS LOS OBJETOS QUE ESTAN GUARDADOS EN FAMILIAR EN LA BASE DE DATOS.
   
    template = loader.get_template('ver_familiares.html')
    template_renderizado = template.render({'familiares': familiares})

    return HttpResponse(template_renderizado)

