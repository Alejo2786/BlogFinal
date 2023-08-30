from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .utils import get_countries_from_api

class RegistrationForm(UserCreationForm):
    country_name = forms.ChoiceField(choices=[])
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country_name'].choices = [(country, country) for country in get_countries_from_api()]

    class Meta:
        model = UserProfile
        fields = ('username', 'password1', 'password2', 'country_name', 'email', 'first_name', 'last_name')
