from django.db import models
from django.conf import settings
from django.db.models import Model 
import uuid

class Sobre(models.Model):
    id_sobre = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logo = models.ImageField()
    descricao = models.TextField()
    foto = models.ImageField()