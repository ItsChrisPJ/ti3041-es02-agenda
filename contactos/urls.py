from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto_list, name='contacto_list'),
    path('nuevo/', views.contacto_create, name='contacto_create'),
]
