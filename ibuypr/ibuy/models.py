from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Categoria(models.Model):
    tipo = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.tipo


class Utilizador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.CharField(max_length=100, default='utilizador.png')
    credito = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def total_credito(self):
        return self.credito

    def adicionar_credito(self, value):
        if value >= 0:
            self.credito = self.credito + value
            self.save()

    def remover_credito(self, value):
        if self.credito - value >= 0 and value > 0:
            self.credito = self.credito - value
            self.save()


class Produto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    likes = models.ManyToManyField(User, related_name='likes')
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default="", related_name="Categoria")
    quantidade = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=datetime.now, editable=False)
    descricao = models.TextField()
    preco = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0.00,
    )
    imagem = models.CharField(max_length=100, default='produto.png')
    video_embed = models.CharField(max_length=1000, blank=True)

    NOVO = 'Novo'
    USADO = 'Usado'
    OPCOES_CONDICAO = (
        (NOVO, 'Novo'),
        (USADO, 'Usado'),
    )
    condicao = models.CharField(choices=OPCOES_CONDICAO, default=NOVO, max_length=100)

    def total_likes(self):
        return self.likes.count()


class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    texto = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now, editable=False)

    def total_comentarios(self):
        return self.count()


class HistoricoCompras(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=datetime.now, editable=False)


