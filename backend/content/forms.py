from django import forms 
from .models import Perfil
  
class PerfilForm(forms.ModelForm): 
  
    class Meta: 
        model = Perfil 
        fields = ('nome', 'email', 'cidade', 'profissao', 'linkedin', 'site', 'github', 'facebook', 'biografia', 'foto',)