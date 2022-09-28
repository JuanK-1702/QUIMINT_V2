"""quimint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principal import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Panel administrador
    path('admin/', admin.site.urls),
    # Vista Principal
    path('', views.principal, name='principal'),
    
    # Equipos
    path('equipos/', views.agregarEquipos, name='equipos'),
    # path('todos/', views.mostrarEquipos),
    path('equipo/<int:id>', views.mostrarEquipo, name='equipo'),
    path('eliminar/<int:id>', views.eliminarEquipo, name='eliminar'),
    
    
    path('suministros/', views.agregarSuministros, name='suministros'),
    # path('todos/', views.mostrarEquipos),
    path('suministro/<int:id>', views.mostrarSuministros, name='suministro'),
    # path('actualizar/', views.actualizarEquipo),
    
    
    path('herramientas/', views.agregarHerramientas, name='herramientas'),
    # path('todos/', views.mostrarEquipos),
    path('herramienta/<int:id>', views.mostrarHerramientas, name='herramienta'),
    # path('actualizar/', views.actualizarEquipo),

]
if settings.DEBUG:
  urlpatterns +=static(
      settings.MEDIA_URL, 
      document_root=settings.MEDIA_ROOT
      )
  