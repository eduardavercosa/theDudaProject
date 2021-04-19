from urllib.parse import urljoin

from django.conf import settings
from django.db import models

import requests


class Battle(models.Model):
    url = urljoin(settings.POKE_API_URL, "?limit=1000")
    response = requests.get(url)
    data = response.json()

    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="+",
        verbose_name="You are:",
        null=True,
    )
    opponent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="+",
        verbose_name="Opponent:",
        null=True,
    )
    c_pokemon_1 = models.CharField(max_length=200, verbose_name="Pokemon 1:", null=True)
    c_pokemon_2 = models.CharField(max_length=200, verbose_name="Pokemon 2:", null=True)
    c_pokemon_3 = models.CharField(max_length=200, verbose_name="Pokemon 3:", null=True)
    o_pokemon_1 = models.CharField(max_length=200, verbose_name="Pokemon 1:", null=True)
    o_pokemon_2 = models.CharField(max_length=200, verbose_name="Pokemon 2:", null=True)
    o_pokemon_3 = models.CharField(max_length=200, verbose_name="Pokemon 3:", null=True)

    def publish(self):
        self.save()
