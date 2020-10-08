from django.db import models
from django.conf import settings
from django.db.models import Model 
import uuid

class Sobre(models.Model):
    id_sobre = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logo = models.ImageField()
    descricao = models.TextField()
    foto = models.ImageField()

class Eventos(models.Model):
    id_evento = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_inicial = models.DateField()
    data_final = models.DateField(null=True, blank=True)
    titulo = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    link = models.URLField(max_length=200, default = ' ')
