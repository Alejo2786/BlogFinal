from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .utils import get_countries_from_api
from django.core.cache import cache
from .models import Comment


class RegistrationForm(UserCreationForm):
    country_name = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country_name'].choices = self.get_cached_countries()

    def get_cached_countries(self):
        cached_countries = cache.get('countries')

        if cached_countries is None:
            cached_countries = get_countries_from_api()
            cached_countries.sort()  # Ordena la lista alfabéticamente
            cache.set('countries', cached_countries, 3600)  # Almacenar en caché por 1 hora

        return [(country, country) for country in cached_countries]
    class Meta:
        model = UserProfile
        fields = ('username', 'password1', 'password2', 'country_name', 'email', 'first_name', 'last_name')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']