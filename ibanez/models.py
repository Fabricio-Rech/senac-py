from django.db import models

class Tipo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    emEstoque = models.BooleanField()
    preco = models.IntegerField()
    data_lanc = models.DateField()
    slug = models.SlugField()
    foto = models.ImageField(upload_to='imagens/%Y/%m/%D')
    
    def __str__(self):
        return self.nome
    