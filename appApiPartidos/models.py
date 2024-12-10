from django.db import models

class Partidos(models.Model):

    CATEGORIA_CHOICES = [
        ('primera A', 'Primera A'),
        ('primera B', 'Primera B'),
    ]

    categoria = models.CharField(
        max_length=100,
        choices=CATEGORIA_CHOICES,  
    )
    fecha = models.DateField()
    hora = models.TimeField()
    equipoLocal = models.CharField(max_length=100)
    equipoVisitante = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.equipoLocal} vs {self.equipoVisitante}"
