from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto_list, name='contacto_list'),
    path('nuevo/', views.contacto_create, name='contacto_create'),
    path('editar/<int:pk>/', views.contacto_update, name='contacto_update'),
    path('eliminar/<int:pk>/', views.contacto_delete, name='contacto_delete'),
]
