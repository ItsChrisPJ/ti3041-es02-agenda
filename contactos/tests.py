from django.test import TestCase
from django.urls import reverse
from .models import Contacto
from .forms import ContactoForm


class ContactoModelTest(TestCase):
    def setUp(self):
        self.contacto = Contacto.objects.create(
            nombre="Ana Torres",
            telefono="+56987654321",
            correo="ana.torres@inacap.cl",
            direccion="Av. Los Carrera 123"
        )

    def test_contacto_str(self):
        self.assertEqual(str(self.contacto), "Ana Torres (ana.torres@inacap.cl)")


class ContactoFormTest(TestCase):
    def test_form_valido(self):
        form = ContactoForm(data={
            'nombre': 'Pedro Pascal',
            'telefono': '+56912345678',
            'correo': 'pedro.pascal@correo.com',
            'direccion': 'Santiago Centro'
        })
        self.assertTrue(form.is_valid())

    def test_form_nombre_demasiado_corto(self):
        form = ContactoForm(data={
            'nombre': 'Al',
            'telefono': '+56912345678',
            'correo': 'al@correo.com',
            'direccion': 'Calle 1'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('nombre', form.errors)


class ContactoViewsTest(TestCase):
    def setUp(self):
        self.contacto = Contacto.objects.create(
            nombre="Lucas Silva",
            telefono="+56999887766",
            correo="lucas@inacap.cl",
            direccion="Providencia 400"
        )

    def test_contacto_list_view(self):
        response = self.client.get(reverse('contacto_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lucas Silva")

    def test_contacto_create_view(self):
        response = self.client.post(reverse('contacto_create'), {
            'nombre': 'Valeria Ríos',
            'telefono': '+56911223344',
            'correo': 'valeria@correo.cl',
            'direccion': 'Las Condes 800'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Contacto.objects.filter(correo='valeria@correo.cl').exists())

    def test_contacto_update_view(self):
        response = self.client.post(reverse('contacto_update', args=[self.contacto.pk]), {
            'nombre': 'Lucas Silva Modificado',
            'telefono': '+56999887766',
            'correo': 'lucas@inacap.cl',
            'direccion': 'Providencia 500'
        })
        self.assertEqual(response.status_code, 302)
        self.contacto.refresh_from_db()
        self.assertEqual(self.contacto.nombre, 'Lucas Silva Modificado')

    def test_contacto_delete_view(self):
        response = self.client.post(reverse('contacto_delete', args=[self.contacto.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Contacto.objects.filter(pk=self.contacto.pk).exists())
