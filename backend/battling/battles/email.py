from urllib.parse import urljoin

from django.conf import settings
from django.urls import reverse

from templated_email import send_templated_mail


def send_battle_result(battle, winner, creator_pkms, opponent_pkms):
    battle_detail_path = reverse("fights", args=None)
    battle_details_url = urljoin(settings.HOST, battle_detail_path)
    send_templated_mail(
        template_name="battle_result",
        from_email="eduardavercosa@vinta.com.br",
        recipient_list=[battle.player1.email, battle.player2.email],
        context={
            "name": "eduarda",
            "battle_creator": battle.player1.email.split("@")[0],
            "battle_opponent": battle.player2.email.split("@")[0],
            "battle_winner": winner,
            "battle_id": battle.id,
            "creator_team": [
                creator_pkms[0]["name"],
                creator_pkms[1]["name"],
                creator_pkms[2]["name"],
            ],
            "opponent_team": [
                opponent_pkms[0]["name"],
                opponent_pkms[1]["name"],
                opponent_pkms[2]["name"],
            ],
            "battle_details_url": battle_details_url,
        },
    )
