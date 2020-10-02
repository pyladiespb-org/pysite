from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.sobre_view, name='sobre_view'),
    path('sobre/', views.sobre_detalhe, name='sobre_detalhe')
] 
  
