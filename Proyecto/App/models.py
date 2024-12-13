# App/models.py

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()  # Campo para la descripción
    imagen = models.ImageField(upload_to='imagenes/')  # Campo para la imagen

    def __str__(self):
        return self.nombre

class Reseña(models.Model):
    nombre_persona = models.CharField(max_length=100)
    estrellas = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    comentario = models.TextField()

    def __str__(self):
        return f"{self.nombre_persona} - {self.producto.nombre} - {self.estrellas} estrellas"

class Carrito(models.Model):
    productos = models.ManyToManyField(Producto, through='CarritoProducto')

    def __str__(self):
        return f'Carrito {self.id}'

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad}'
    

class Schedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date} at {self.time}"

# App/models.py

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('reiki', 'Reiki'),
        ('tarot', 'Tarot'),
        ('flowers', 'Terapia de Flores'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=10, choices=SERVICE_CHOICES, default='reiki')

    def __str__(self):
        return f"Booking for {self.name} on {self.schedule}"