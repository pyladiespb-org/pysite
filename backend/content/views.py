from django.shortcuts import render
from .models import Sobre
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Eventos
from .models import Perfil


def base_view(request):
    return render(request, 'content/base.html', {})

def sobre_detalhe(request):
    sobre = get_object_or_404(Sobre)
    return render(request, 'content/sobre_detalhe.html', {'sobre': sobre})

def eventos_list(request):
    eventos = Eventos.objects.filter(data_inicial__gte=timezone.now()).order_by('data_inicial')
    return render(request, 'content/eventos_list.html', {'eventos': eventos})

def perfis_list(request):
    perfis = Perfil.objects.all()
    return render(request, 'content/perfis_list.html', {'perfis': perfis})