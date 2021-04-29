from django.db import models

from pokemon.models import Pokemon
from users.models import User


class Battle(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator_battles")
    opponent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="opponent_battles")

    creator_pokemon_1 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="+")
    creator_pokemon_2 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="+")
    creator_pokemon_3 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="+")

    opponent_pokemon_1 = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, related_name="+", null=True
    )
    opponent_pokemon_2 = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, related_name="+", null=True
    )
    opponent_pokemon_3 = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, related_name="+", null=True
    )

    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="battle_win", null=True)
