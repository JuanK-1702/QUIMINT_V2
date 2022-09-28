
from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from urllib.request import Request
from django.shortcuts import render, redirect

from principal.models import Equipos
from .forms import *
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.

# Session Principal de la pagina
def principal(request):
    return render(request, 'pages/principal.html')


# CRUD de equipos
'''
Funcion para agregar equipos y retorno de mensajes
'''
def agregarEquipos(request):
    equipos = Equipos.objects.all()
    if request.method == 'POST':
        form = formEquipos(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Por fin")
            return HttpResponseRedirect('/')
        else:
            return render(request, 'pages/equipos.html', {'form': form })
    else: 
        form = formEquipos()
    data={
            'form': form,
            'equipos':equipos
        }
    return render(request, 'pages/equipos.html',data)


# '''
# Funcion Mostrar solo un equipo
# '''
def mostrarEquipo(request, id):
    equipo = Equipos.objects.get(id=id)
    if request.method == 'GET':
        form = formEquipos(instance=equipo)
        data={
            'equipo':equipo,
            'form': form,
            'id': id
        }
        return render(request, 'pages/equipo.html',data)
    
    if request.method == 'POST':
        form = formEquipos(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
        data={
            'equipo':equipo,
            'form': form,
            'id': id
        }   
        return render(request, 'pages/equipo.html',data)


'''
Funcion Eliminar equipo
'''
def eliminarEquipo(request, id):
    equipos = Equipos.objects.get(id=id)
    equipos.delete()
    return redirect('equipos')


# def actualizarEquipo(request, id):
#     equipo = Equipos.objects.get(id=id)
#     if request.method == 'GET':
#         form = Equipos(instance = equipo)
#         data ={
#            'form': form,
#            'id': id
#         }
#         return render(request, 'pages/equipo.html',data)
    
#     if request.method == 'POST':
#         form = Equipos(request.POST, instance = equipo)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Envio exitoso')
#         else:
#             messages.warning(request, 'Error')
#         return HTTPResponse(Request.POST)





# CRUD de Suministros
'''
Funcion para agregar suministros y retorno de mensajes
'''
def agregarSuministros(request):
    suministros = Suministros.objects.all()
    if request.method == 'POST':
        form = formSuministros(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Suministro Agregado Correctamente')
            return HttpResponseRedirect('/')
        else:
            return render(request, 'pages/suministros.html', {'form': form})
    else:
        form = formSuministros()
    data = {
        'form': form,
        'equipos': suministros
    }
    return render(request, 'pages/suministros.html', data)
#def agregarSuministros(request):
    #suministros = Suministros.objects.all()
    #if request.method == 'POST':
        #form = formSuministros(request.POST, request.FILES)
        #if form.is_valid():
            #form.save()
            #messages.success(request, "Por fin")
            #return HttpResponseRedirect('/')
        #else:
            #messages.error(request, "error")
    #else:
        #form = formSuministros()    
    #data={
        #'form': form,
        #'suministros':suministros
    #}
    #return render(request, 'pages/suministros.html',data)


# '''
# Funcion Mostrar solo un equipo
# '''
def mostrarSuministros(request, id):
    suministros = Suministros.objects.get(id=id)
    if request.method == 'GET':
        form = formSuministros(instance=suministros)
        data={
            'suministros':suministros,
            'form':form,
            'id':id
        }
        return render(request, 'pages/suministros.html',data)

    if request.method == 'POST':
        form = formSuministros(request.POST, request.FILES, instance=suministros)
        if form.is_valid():
            form.save()
        data={
            'suministro': suministros,
            'form': form,
            'id': id 
        }
        return render(request, 'pages/suministro.html', data)
    
'''
Funcion Eliminar Suministro
'''
def eliminarSuministro(request, id):
    suministros = Suministros.objects.all()
    suministros.delete()
    return redirect('equipos')
    



# CRUD de Herramientas

'''
Funcion para agregar equipos y retorno de mensajes
'''
def agregarHerramientas(request):
    herramientas = Herramientas.objects.all()
    if request.method == 'POST':
        form = formHerramientas(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Herramienta Agregada Correctamente")
            return HttpResponseRedirect('/')
        else:
            return render(request, 'pages/herramientas.html', {'form': form })
    else:
        form = formHerramientas()
    data={
        'form': form,
        'herramientas':herramientas
    }
    return render(request, 'pages/herramientas.html',data)



# '''
# Funcion Mostrar solo un equipo
# '''
def mostrarHerramientas(request, id):
    herramienta = Herramientas.objects.get(id=id)
    if request.method == 'GET':
        form = formHerramientas(instance=herramienta)
        data={
            'herramienta':herramienta,
            'form': form,
            'id': id
        }
        return render(request, 'pages/herramienta.html',data)
    
    if request.method == 'POST':
        form = formHerramientas(request.POST, request.FILES, instance=herramienta)
        if form.is_valid():
            form.save()
        data={
            'herramienta':herramienta,
            'form': form,
            'id': id
        }   
        return render(request, 'pages/herramienta.html',data)
    
'''
Funcion Eliminar Herramienta
'''
def eliminarHerramienta(request, id):
    herramientas = Herramientas.objects.get(id=id)
    herramientas.delete()
    return redirect('equipos')