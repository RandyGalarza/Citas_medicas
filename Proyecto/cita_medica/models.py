from django.db import models

class ReservaCita(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    estado = models.CharField(max_length=20)
    tipo_cita = models.CharField(max_length=50)
    def __str__(self):
        return f'Cita médica para {self.nombre_paciente} el {self.fecha_cita} a las {self.hora_cita}'


class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_paciente
    
class Medico(models.Model):
    nombre_medico = models.CharField(max_length=100)
    especialidad= models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_medico