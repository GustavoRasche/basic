from django.db import models

# Create your models here.
class Usuario(models.Model): 
    
    idUsuario = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    rutC = models.CharField(max_length=12, null=False)
    nombre = models.CharField(max_length=100, null=False, unique=True )
    apellidoPaterno = models.CharField(max_length=45, null=False)
    correo = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=50, null=False)
    
    
    def todo(self):
        return Usuario
    
    
class Empleado(models.Model):
    idEmpleado = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Codigo Empleado')
    correo = models.CharField(max_length=50, null=False)
    contraseña = models.CharField(max_length=8)