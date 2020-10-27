from django.contrib import admin
from .models import Sobre
from .models import Evento
from .models import Perfil
from .models import Atividade
from .models import EventoAgendado

admin.site.register(Sobre)
admin.site.register(EventoAgendado)
admin.site.register(Perfil)
admin.site.register(Atividade)
admin.site.register(Evento)