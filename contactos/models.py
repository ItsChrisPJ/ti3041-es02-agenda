from django.db import models
from django.core.validators import EmailValidator

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(
        validators=[EmailValidator(message="El formato del correo electrónico no es válido.")],
        unique=True
    )
    direccion = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.nombre} ({self.correo})"
