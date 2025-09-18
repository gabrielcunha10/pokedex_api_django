from django.forms import forms
from .models import PokemonFavorito

class PokemonFavoritoForm(forms.modelForm):
    class Meta:
        model = PokemonFavorito
        fields = ['nomepokemon']
        