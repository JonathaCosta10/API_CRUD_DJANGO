from django.contrib import admin
from django.urls import path, include
from CRUD_APP import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CRUD_APP.urls')),  # Corrigido para incluir as URLs do aplicativo CRUD
]
