from urllib.parse import urljoin

from django.conf import settings

import requests

from pokemons.models import Pokemon


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


def save_pokemon(poke_name):
    pokemon = Pokemon.objects.filter(name=poke_name).first()

    if pokemon:
        return pokemon

    data = get_pokemon_from_api(poke_name)

    return Pokemon.objects.create(
        pokemon_id=data["poke_id"],
        name=data["name"],
        img_url=data["img_url"],
        defense=data["defense"],
        attack=data["attack"],
        hp=data["hp"],
    )


def valid_team(pokemons):
    points = 0
    for poke_name in pokemons:
        pokemon = Pokemon.objects.filter(name=poke_name).first()
        points += pokemon.attack + pokemon.defense + pokemon.hp

    return points <= 600
