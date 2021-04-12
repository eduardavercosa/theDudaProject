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


def sumValid(pokemon):
    sum_result = pokemon["attack"] + pokemon["defense"] + pokemon["hp"]
    return sum_result


def check_valid_team1(curr_form):
    pokemon1 = get_pokemon_from_api(curr_form.pk11)
    pokemon2 = get_pokemon_from_api(curr_form.pk12)
    pokemon3 = get_pokemon_from_api(curr_form.pk13)
    sum_pokemons_points = sumValid(pokemon1) + sumValid(pokemon2) + sumValid(pokemon3)
    if sum_pokemons_points <= 600:
        return True
    return False


def check_valid_team2(curr_form):
    pokemon1 = get_pokemon_from_api(curr_form.pk21)
    pokemon2 = get_pokemon_from_api(curr_form.pk22)
    pokemon3 = get_pokemon_from_api(curr_form.pk23)
    sum_pokemons_points = sumValid(pokemon1) + sumValid(pokemon2) + sumValid(pokemon3)
    if sum_pokemons_points <= 600:
        return True
    return False
