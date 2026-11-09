from django.db import models

# Create your models here.
class Tarefa(models.Model):
    PRIORIDADES = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baixa', 'Baixa')
    ]
    titulo = models.CharField(max_length=120)
    descricao = models.TextField(blank=True, null=True)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
