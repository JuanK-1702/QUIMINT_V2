
from email.policy import default
from random import choices
from django.utils import timezone
from django.db import models

ESTADOS = (
    ('Disponible','Disponible'),
    ('Agotado','Agotado'),
    ('Escaso','Escaso'),
)
AREA = (
    ('Linea Sulfurico','Linea Sulfurico'),
    ('Linea Sulfurico 2','Linea Sulfurico 2'),
    ('Linea Fosforico','Linea Fosforico'),
    ('Linea Fosforita','Linea Fosforita'),
    ('Linea D','Linea D'),
    ('Linea Mantenimiento','Linea Mantenimiento'),
    ('Linea Raymon','Linea Raymon'),
    ('Linea Mezclas','Linea Mezclas'),
    ('Linea Horno','Linea Horno'),
    ('Linea Dolomita','Linea Dolomita'),
)
OCUPACION = (
    ('Almacen','Almacen'),
    ('Taller','Taller'),
)

# Create your models here.
class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)
       
    def __str__(self):
        return self.tipo
    
class Equipos(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=timezone.now)
    nombre = models.CharField(max_length=20) 
    referencia = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, null=True, choices=ESTADOS, default='Disponible')
    cantidad = models.IntegerField()
    ordenEmitida = models.CharField(max_length=20) 
    solicitudDeMantenimiento = models.CharField(max_length=20) 
    ocupadoenArea = models.CharField(max_length=20, null=True, choices=OCUPACION, default='Almacen')
    enviadoalArea = models.CharField(max_length=20, null=True, choices=AREA, default='Linea Sulfurico')
    observaciones = models.CharField(max_length=20) 
    imagenE = models.ImageField(upload_to="equipos", null= True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    marca = models.CharField(max_length=20)
    valorU = models.FloatField(max_length=20)
    costo = models.FloatField(max_length=20)
    
    def __str__(self):
        return self.repuesto
    
class Suministros(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=timezone.now)
    nombre = models.CharField(max_length=20)
    referencia = models.CharField(max_length=20, null=True, choices=ESTADOS, default='Disponible')
    estado = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    ordenEmitida = models.CharField(max_length=20)
    solicituDeMantenimiento = models.CharField(max_length=20)
    ocupadoenArea = models.CharField(max_length=20, null=True, choices=OCUPACION, default='Almacen')
    enviadoalArea = models.CharField(max_length=20, null=True, choices=AREA, default='Linea Sulfurico')
    observaciones = models.CharField(max_length=100)
    imagenS = models.ImageField(upload_to="suministros", null= True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    marca = models.CharField(max_length=20)
    valorU = models.FloatField(max_length=20)
    costo = models.FloatField(max_length=20)
    
    def __str__(self):
        return self.repuesto
    
class Herramientas(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=timezone.now)
    nombre = models.CharField(max_length=20)
    referencia = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, null=True, choices=ESTADOS, default='Disponible')
    cantidad = models.FloatField(max_length=20)
    ordenEmitida = models.CharField(max_length=20)
    solicitudDeMantenimiento = models.CharField(max_length=20)
    ocupadoenArea = models.CharField(max_length=20, null=True, choices=OCUPACION, default='Almacen')
    enviadoalArea = models.CharField(max_length=20, null=True, choices=AREA, default='Linea Sulfurico')
    observaciones = models.CharField(max_length=100)
    imagenH = models.ImageField(upload_to="herramientas", null= True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    marca = models.CharField(max_length=20)
    valorU = models.FloatField(max_length=20)
    costo = models.FloatField(max_length=20) 
    
    def __str__(self):
        return self.repuesto
    
class ReporteInventario(models.Model):
    id = models.AutoField(primary_key=True)
    equipos = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    suministros = models.ForeignKey(Suministros, on_delete=models.CASCADE)
    herramientas = models.ForeignKey(Herramientas, on_delete=models.CASCADE)