from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    nascimento = models.DateField()
    email = models.EmailField()
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nome