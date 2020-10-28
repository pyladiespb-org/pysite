from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.base_view, name='base_view'),
    path('sobre/', views.sobre_detalhe, name='sobre_detalhe'),
    path('eventos/', views.eventos_list, name='eventos_list'),
    path('perfis/', views.perfis_list, name='perfis_list'),
    path('perfis/novo/', views.perfil_novo, name='perfil_novo'),
    path('pyladies-day/', views.pyladiesday_eventos, name='pyladiesday_eventos'),
] 
