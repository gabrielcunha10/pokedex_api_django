from django.db import models
from django.contrib.auth.models import User

class PokemonFavorito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nomepokemon = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.nomepokemon}"
        
    


