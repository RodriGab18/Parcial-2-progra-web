from django.db import models


class Tarea(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
    ]

    titulo = models.CharField(max_length=200)
    curso = models.CharField(max_length=100)
    fechaEntrega = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='pendiente',
    )

    def __str__(self):
        return f"{self.titulo} - {self.get_estado_display()}"