from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'correo', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej. Juan Pérez'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ej. +56912345678'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ej. Av. Siempreviva 742'}),
        }
