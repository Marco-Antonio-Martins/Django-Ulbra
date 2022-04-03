from tabnanny import verbose
from django.db import models
from django.utils import timezone

class Noticia(models.Model):
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias' 
    titulo = models.CharField('Título', max_length=120, null=True)
    conteudo = models.TextField('Conteúdo')
    data_publicacao = models.DateField("Data da Publicação", null=True)