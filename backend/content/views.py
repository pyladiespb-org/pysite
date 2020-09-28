from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
  
 
def sobre_view(request): 
  
    if request.method == 'POST': 
        form = SobreForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = SobreForm() 
    return render(request, 'sobre.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 