from urllib.parse import urljoin

from django.conf import settings
from django.urls import reverse

from templated_email import send_templated_mail


def send_battle_result(battle, creator_pokemon_list, opponent_pokemon_list):
    battle_detail_path = reverse("battle_details", args=None)
    battle_details_url = urljoin(settings.HOST, battle_detail_path)
    send_templated_mail(
        template_name="battle_result",
        from_email="eduardavercosa@vinta.com.br",
        recipient_list=[battle.creator.email, battle.opponent.email],
        context={
            "battle_creator": battle.creator.email.split("@")[0],
            "battle_opponent": battle.opponent.email.split("@")[0],
            "battle_winner": battle.winner.email.split("@")[0],
            "battle_id": battle.id,
            "creator_team": [
                creator_pokemon_list[0]["name"],
                creator_pokemon_list[1]["name"],
                creator_pokemon_list[2]["name"],
            ],
            "opponent_team": [
                opponent_pokemon_list[0]["name"],
                opponent_pokemon_list[1]["name"],
                opponent_pokemon_list[2]["name"],
            ],
            "battle_details_url": battle_details_url,
        },
    )
