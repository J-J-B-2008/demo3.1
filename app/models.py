from django.db import models
from grupo.models import Group


class Montadora(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Unidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Grupo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Fabricante(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
            

class Produtos(models.Model):
    codigo = models.CharField(max_length=255) 
    original = models.CharField(max_length=255, null=True, blank=True)    
    descricao = models.CharField(max_length=255)
    aplicacao = models.CharField(max_length=255)
    montadora = models.ForeignKey(Montadora, on_delete=models.PROTECT, related_name='chave_montadora')
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name='chave_unidade')
    grupo = models.ForeignKey(Group, blank=True, null=True, on_delete=models.PROTECT, related_name='chave_grupo')
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT, related_name='chave_fabricante') 
    imagem1 = models.ImageField(upload_to='medeia/', blank=True, null=True)

    def __str__(self):
        return self.codigo

