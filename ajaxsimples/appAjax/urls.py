from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #aqui fazemos nosso apontamento raíz para nosso index na view do appAjax.
    path('ajax', views.filtroAjax, name='ajax'), #essa url é responsável por receber os valores do ajax
]
