from django.db import models

class Usuarios(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    cpf = models.IntegerField()
    senha = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.nome