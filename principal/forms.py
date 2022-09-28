
from dataclasses import fields
from django import forms
from django.core.validators import RegexValidator

from .models import *
class formEquipos(forms.ModelForm):
    
    # fecha = forms.DateField(label='Birthday', widget=forms.DateInput(attrs={'placeholder': 'Enter your birthday', 'type': 'date'}))
                    
    # repuesto = forms.CharField(
    #     label='Repuesto', min_length=3, max_length=30,
    #     validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    #     message="solo se permite letras")],
    #     widget=forms.TextInput(attrs={'placeholder':'Repuesto'}))
    
    # referencia = forms.CharField(
    #     label='Referencia', min_length=3, max_length=30,
    #     validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    #     message="solo se permite letras")],
    #     widget=forms.TextInput(attrs={'placeholder':'Referencia'})
    # )
    
    # estado = forms.CharField(
    #     label='Estado', min_length=3, max_length=30,
    #     validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    #     message="solo se permite letras")],
    #     widget=forms.TextInput(attrs={'placeholder':'Estado'})
    # )
    
    # cantidad = forms.CharField(
    #     label='Cantidad',
    #     validators=[RegexValidator(r'^[0-9]*$',
    #     message="solo se permite Numeros")],
    #     widget=forms.TextInput(attrs={'placeholder':'Cantidad'})
    # )
    
    # entrada = forms.CharField(
    #     label='Entrada',
    #     validators=[RegexValidator(r'^[0-9]*$',
    #     message="solo se permite Numeros")],
    #     widget=forms.TextInput(attrs={'placeholder':'Entrada'})
    # )
    
    # salida = forms.CharField(
    #     label='Salida',
    #     validators=[RegexValidator(r'^[0-9]*$',
    #     message="solo se permite Numeros")],
    #     widget=forms.TextInput(attrs={'placeholder':'Salida'})
    # )
    
    # ocupacionenArea = forms.CharField(
    #     label='Ocupaciones', min_length=3, max_length=40,
    #     validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    #     message="solo se permite letras")],
    #     widget=forms.TextInput(attrs={'placeholder':'Ocupaciones'})
    # )
    
    # especificaciones = forms.CharField(
    #     label='Especificaciones', min_length=3, max_length=40,
    #     validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    #     message="solo se permite letras")],
    #     widget=forms.Textarea(attrs={'placeholder':'Especificaciones'})
    # )
    
    # imagenH = forms.ImageField(
    #     label='Imagen',
    #     widget=forms.TextInput(attrs={'placeholder':'Imagen'})
    # )
    
    # categoria = forms.CharField(
    #     label='Categoria', min_length=3, max_length=40,
    #     validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    #     message="solo se permite letras")],
    #     widget=forms.TextInput(attrs={'placeholder':'Categoria'})
    # )
    
    # marca = forms.CharField(
    #     label='Marca', min_length=3, max_length=40,
    #     validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    #     message="solo se permite letras")],
    #     widget=forms.TextInput(attrs={'placeholder':'Marca'})
    # )
    
    # valorU = forms.CharField(
    #     label='Valor',
    #     validators=[RegexValidator(r'^[0-9]*$',
    #     message="solo se permite Numeros")],
    #     widget=forms.TextInput(attrs={'placeholder':'Valor'})
    # )
    
    # costo = forms.CharField(
    #     label='Costo',
    #     validators=[RegexValidator(r'^[0-9]*$',
    #     message="solo se permite Numeros")],
    #     required= False,
    #     widget=forms.TextInput(attrs={'placeholder':'Costo'})
    # )
    
    class Meta:
        model = Equipos
        fields = "__all__"
        # widgets = {
        #     'cantidad' :forms.TextInput(attrs={'placeholder':'Cantidad','data-mask': '(00) 00000-0000'})
        # }
    
class formSuministros(forms.ModelForm):
    
    class Meta:
        model = Suministros
        fields = "__all__"
        
        
class formHerramientas(forms.ModelForm):
    
    class Meta:
        model = Herramientas
        fields = "__all__"