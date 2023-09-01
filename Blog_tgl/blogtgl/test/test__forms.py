from django.test import TestCase
from blogtgl.forms import RegistrationForm, CommentForm

class RegistrationFormTest(TestCase):
    def test_valid_registration_form(self):
        # Datos de prueba válidos
        data = {
            'username': 'usuario',
            'password1': 'contraseña123',
            'password2': 'contraseña123',
            'country_name': 'Colombia',
            'email': 'usuario@example.com',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }

        form = RegistrationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_registration_form(self):
        # Datos de prueba inválidos (contraseñas no coinciden)
        data = {
            'username': 'usuario',
            'password1': 'contraseña123',
            'password2': 'contraseña456',  # Contraseña diferente
            'country_name': 'País',
            'email': 'usuario@example.com',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }

        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

class CommentFormTest(TestCase):
    def test_valid_comment_form(self):
        # Datos de prueba válidos para el formulario de comentario
        data = {
            'text': 'Este es un comentario válido.',
        }

        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_comment_form(self):
        # Datos de prueba inválidos para el formulario de comentario (texto vacío)
        data = {
            'text': '',
        }

        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())

