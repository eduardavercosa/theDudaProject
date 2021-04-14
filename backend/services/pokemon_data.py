from urllib.parse import urljoin

from django.conf import settings

import requests


def get_pokemon_from_api(poke_name):
    url = urljoin(settings.POKE_API_URL, poke_name.lower())
    response = requests.get(url)
    data = response.json()
    info = {
        "poke_id": data["id"],
        "name": data["name"],
        "defense": data["stats"][3]["base_stat"],
        "attack": data["stats"][4]["base_stat"],
        "hp": data["stats"][5]["base_stat"],
    }
    return info


def team_points(pokemons):
    points = 0
    for pokemon in pokemons:
        points += pokemon["attack"] + pokemon["defense"] + pokemon["hp"]
    return points


def valid_team(round_battle, player):
    pokemons_id = [getattr(round_battle, player + "_pokemon_" + str(i)) for i in range(1, 4)]
    pokemons = [get_pokemon_from_api(pokemon) for pokemon in pokemons_id]

    is_valid = team_points(pokemons) <= 600
    return is_valid
