from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    def __str__(self):
        return self.nome