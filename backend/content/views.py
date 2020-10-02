from django.shortcuts import render
from .models import Sobre
from django.shortcuts import render, get_object_or_404

def sobre_view(request):
    sobre = Sobre.objects.all()
    return render(request, 'content/sobre.html', {'sobre':sobre})

def sobre_detalhe(request):
    sobre = get_object_or_404(Sobre)
    return render(request, 'content/sobre_detalhe.html', {'sobre': sobre})