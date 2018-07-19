from datetime import datetime
from django.db import models

class artigo(models.Model):
	class Meta:
		ordering = ('-publicacao',)

	titulo = models.CharField(max_length=100)
	conteudo = models.TextField()
	publicacao = models.DateTimeField(
		default=datetime.now,
		blank=True
		)

class comentario(models.Model):
	class Meta:
		ordering = ('-data',)

	nome = models.CharField(max_length=100)
	comentario = models.TextField()
	data = models.DateTimeField(
		default=datetime.now,
		blank=True
		)