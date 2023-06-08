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

class Pedido(models.Model):
    idPedido = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    estadoP = models.CharField(max_length=50, null=False)
    fechaIngreso = models.DateTimeField(null=False)
    descripcion = models.CharField(max_length=255)
    precio = models.IntegerField(null=False)
    
    
    def __str__(self):
        return self.estadoP
    

class Producto(models.Model):
    idProducto =  models.BigIntegerField(auto_created=True, primary_key=True,  serialize=False, verbose_name='Codigo Producto')
    tipo = models.CharField(max_length=45, null=False)
    descripcion = models.CharField(max_length=255)
    valor = models.CharField(max_length=45)
    
    

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.tipo
    

class Envio(models.Model):
    idEnvio = models.BigIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='Codigo Envio')
    direccion = models.CharField(max_length=50)
    estado = models.IntegerField()
    

    class Meta:
        verbose_name = ("Envio")
        verbose_name_plural = ("Envios")

    def __str__(self):
        return self.idEnvio

class Historial(models.Model):
    idHistorial = models.BigIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='Historial Pedidos')
    pedido = models.ForeignKey(Pedido, null=True, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Historial")
        verbose_name_plural = ("Historiales")

    def __str__(self):
        return self.name


    