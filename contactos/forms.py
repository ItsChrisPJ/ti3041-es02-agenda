from django import forms
import re
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'correo', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Juan Pérez'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. +56 9 1234 5678'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Av. Siempre Viva 742'
            }),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono', '').strip()
        # Permite dígitos, espacios, +, - y paréntesis
        if not re.match(r'^[0-9+\-\s\(\)]+$', telefono):
            raise forms.ValidationError("El teléfono contiene caracteres no válidos.")
        if len(re.sub(r'\D', '', telefono)) < 8:
            raise forms.ValidationError("El número telefónico debe tener al menos 8 dígitos.")
        return telefono
