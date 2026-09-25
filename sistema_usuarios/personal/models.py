from django.db import models

# 1. Modelo Departamento
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


# 2. Modelo Cargo
class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


# 3. Modelo Empleado
class Empleado(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    
    # Relaciones con Django ORM (Foreign Keys)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Activo')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"