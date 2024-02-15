from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),  # Rota de cadastro
    path('logar/', views.logar, name='logar'),  # Rota de login
    path('sair/', views.sair, name='sair'),

]
