from django.contrib.auth.models import User
from django.db import models


class Usuario(models.Model):
    vinculado = models.ForeignKey(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11, default="00000000000")
    cpf = models.CharField(max_length=11, default="11111111111")
