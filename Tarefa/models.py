from django.db import models

from Usuario.models import Usuario


class Tarefa(models.Model):
    vinculo = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=20, default="titulo")
    descricao = models.CharField(max_length=150, default="descicao")
    data_vencimento = models.DateField()  # ano/mes/dia
    prioridade = models.IntegerField(default=1)
