from battling.models import Battle
from pokemon.models import Pokemon
from services.email import send_battle_result


def battle_round(creator_pokemon, opponent_pokemon):
    round_score = {"creator": 0, "opponent": 0}

    # Creator's pokemon attacks
    if creator_pokemon["attack"] > opponent_pokemon["defense"]:
        round_score["creator"] += 1
    else:
        round_score["opponent"] += 1

    # Opponents's pokemon attacks
    if opponent_pokemon["attack"] > creator_pokemon["defense"]:
        round_score["creator"] += 1
    else:
        round_score["opponent"] += 1

    #  In case of draw
    if round_score["creator"] == round_score["opponent"]:
        if creator_pokemon["hp"] > opponent_pokemon["hp"]:
            round_score["creator"] += 1
        else:
            round_score["opponent"] += 1

    # Final Round Score
    creator_won = {"creator": 1, "opponent": 0}
    opponent_won = {"creator": 0, "opponent": 1}

    if round_score["creator"] > round_score["opponent"]:
        return creator_won
    return opponent_won


def get_battle_winner(battle):
    battle_score = {"creator": 0, "opponent": 0}
    battle_info = Battle.objects.filter(id=battle.id).values()[0]

    # get the pokemons ids from the battles
    creator_pokemons_id = [battle_info["creator_pokemon_" + str(i) + "_id"] for i in range(1, 4)]
    opponent_pokemons_id = [battle_info["opponent_pokemon_" + str(i) + "_id"] for i in range(1, 4)]
    # get the pokemons from the DB
    creator_pokemon_list = [Pokemon.objects.filter(id=j).values()[0] for j in creator_pokemons_id]
    opponent_pokemon_list = [Pokemon.objects.filter(id=j).values()[0] for j in opponent_pokemons_id]

    for creator_pokemon, opponent_pokemon in zip(creator_pokemon_list, opponent_pokemon_list):
        score = battle_round(creator_pokemon, opponent_pokemon)

        battle_score["creator"] += score["creator"]
        battle_score["opponent"] += score["opponent"]

    battle.winner = battle.creator if score["creator"] > score["opponent"] else battle.opponent

    send_battle_result(battle, creator_pokemon_list, opponent_pokemon_list)

    return battle.winner


def run_battle_and_send_email(battle_id):
    battle = Battle.objects.get(id=battle_id)
    battle.winner = get_battle_winner(battle)
    battle.save()
    return battle.winner
