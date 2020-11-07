from django.shortcuts import render
from .models import Sobre
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import EventoAgendado
from .models import Perfil
from django.shortcuts import redirect
from .forms import PerfilForm
from .models import Evento

def base_view(request):
    return render(request, 'content/base.html', {})

def sobre_detalhe(request):
    sobre = get_object_or_404(Sobre)
    return render(request, 'content/sobre_detalhe.html', {'sobre': sobre})

def eventos_list(request):
    eventos = EventoAgendado.objects.all().order_by('data_inicial')
    return render(request, 'content/eventos_list.html', {'eventos': eventos})

def perfis_list(request):
    perfis = Perfil.objects.all()
    return render(request, 'content/perfis_list.html', {'perfis': perfis})

def perfil_novo(request):
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            perfil = form.save()
            perfil.save()
            return redirect('perfis_list')
    else:
        form = PerfilForm()
    return render(request, 'content/perfil_novo.html', {'form': form})

def pyladiesday_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'content/pyladiesday_eventos.html', {'eventos': eventos})