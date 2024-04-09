from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_item, name='create_item'),
    path('read/', views.read_item, name='read_item'),
    path('update/', views.update_item, name='update_item'),
    path('delete/', views.delete_item, name='delete_item'),
]
