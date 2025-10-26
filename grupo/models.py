from django.db import models


class Grupo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Group(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome    
