from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.base_view, name='base_view'),
    path('sobre/', views.sobre_detalhe, name='sobre_detalhe'),
    path('eventos/', views.eventos_list, name='eventos_list'),
    path('perfis/', views.perfis_list, name='perfis_list'),
] 
  
