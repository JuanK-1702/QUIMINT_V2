from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
class categoriasAdmin(admin.ModelAdmin):
    pass    
class equiposAdmin(admin.ModelAdmin):
    list_filter = ['estado']
    list_display = ['fecha', 'nombre', 'referencia', 'estados', '_', 'cantidad', 'ordenEmitida', 'enviadoalArea','solicitudDeMantenimiento', 'ocupadoenArea', 'observaciones', 'imagenE', 'categoria', 'marca', 'valorU', 'costo']
    search_fields = ['fecha', 'nombre', 'referencia', 'estado', 'cantidad', 'ordenEmitida', 'enviadoalArea','solicitudDeMantenimiento', 'ocupadoenArea', 'observaciones', 'imagenE', 'categoria', 'marca', 'valorU', 'costo']
    list_per_page: 12
    
    # Funcion para estados
    def _(self, obj):
        if obj.estado == 'Disponible':
            return True
        elif obj.estado == 'Pocas':
            return None
        else: 
            return False
    _.boolean = True
    
    def estados(self, obj):
        if obj.estado == 'Disponible':
            color = '#28a745'
        elif obj.estado == 'Pocas':
            color = '#fea95e'
        else: 
            color = 'red'
        return format_html('<strong><p style = "color:{}">{}</p></strong'.format(color, obj.estado))
    estados.allow_tags = True
        
admin.site.register(Categorias, categoriasAdmin)
admin.site.register(Equipos, equiposAdmin)