from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.sobre_view, name='sobre_view'),
] 
  
