from django.db import models

# Create your models here.
from django.db import models

class Filme(models.Model):
    TIPOS = [("filme", "Filme"),
             ("serie", "Série")]

    titulo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    genero = models.CharField(max_length=80)
    ano = models.PositiveIntegerField()
    assistido = models.BooleanField(default=False)
    nota = models.PositiveSmallIntegerField(
        null=True, blank=True
    )
    criado_em = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.titulo
