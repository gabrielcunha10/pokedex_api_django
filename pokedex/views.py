from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import PokemonFavorito
from .forms import PokemonFavoritoForm
from django.urls import reverse_lazy

class PokemonFavoritoCreateView(CreateView):
    model = PokemonFavorito
    form_class = PokemonFavoritoForm
    template_name = "favorito_form.html"
    success_url = reverse_lazy("favorito_lista.html")

class PokemonFavoritoUpdateView(UpdateView):
    model = PokemonFavorito
    form_class = PokemonFavoritoForm
    template_name = "favorito_atualizar.html"
    success_url = reverse_lazy("favorito_lista.html")

class PokemonFavoritoDeleteView(DeleteView):
    model = PokemonFavorito
    template_name = "confirmar_delete.html"
    success_url = reverse_lazy("favorito_lista.html")

class PokemonFavoritoListView(ListView):
    model = PokemonFavorito
    template_name = "favorito_lista.html"