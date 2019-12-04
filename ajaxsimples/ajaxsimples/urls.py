from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('appAjax.urls')), #fazemos uma inclusão para o acesso seja direcionado para a urls do nosso app.
    path('admin/', admin.site.urls),
]
