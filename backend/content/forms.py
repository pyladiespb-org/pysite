from django import forms 
from .models import Sobre
  
class SobreForm(forms.ModelForm): 
  
    class Meta: 
        model = Sobre 
        fields = ('id_sobre', 'logo', 'descricao', 'foto',)