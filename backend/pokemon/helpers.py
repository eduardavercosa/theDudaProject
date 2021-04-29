from urllib.parse import urljoin

import requests

from pokemon.constants import POKE_API_URL
from pokemon.models import Pokemon


def get_all_pokemon_from_api():
    url = urljoin(POKE_API_URL, "?limit=802")
    response = requests.get(url)
    data = response.json()

    for pokemon in data["results"]:
        save_pokemon(pokemon["name"])


def get_pokemon_from_api(poke_name):
    url = urljoin(POKE_API_URL, poke_name)
    response = requests.get(url)
    data = response.json()
    return {
        "poke_id": data["id"],
        "name": data["name"],
        "img_url": data["sprites"]["front_default"],
        "defense": data["stats"][3]["base_stat"],
        "attack": data["stats"][4]["base_stat"],
        "hp": data["stats"][5]["base_stat"],
    }


def save_pokemon(poke_name):
    data = get_pokemon_from_api(poke_name)

    return Pokemon.objects.create(
        poke_id=data["poke_id"],
        name=data["name"],
        img_url=data["img_url"],
        defense=data["defense"],
        attack=data["attack"],
        hp=data["hp"],
    )


def valid_team(pokemon_names):
    points = 0
    for pokemon_name in pokemon_names:
        pokemon = Pokemon.objects.filter(name=pokemon_name).first()

        points += pokemon.attack + pokemon.defense + pokemon.hp

    return points <= 600
