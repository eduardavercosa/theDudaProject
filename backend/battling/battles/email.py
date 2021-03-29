from urllib.parse import urljoin

from django.conf import settings
from django.urls import reverse

from templated_email import send_templated_mail


def send_battle_result(battle):
    battle_detail_path = reverse("battles:battle-detail", args=(battle.pk,))
    battle_details_url = urljoin(settings.HOST, battle_detail_path)
    send_templated_mail(
        template_name="battle_result",
        from_email=settings.EMAIL_ADDRESS,
        recipient_list=[battle.creator.email, battle.opponent.email],
        context={
            "battle_winner": battle.winner.email.split("@")[0],
            "creator_team": battle.creator.teams.filter(battle=battle.id).first(),
            "opponent_team": battle.opponent.teams.filter(battle=battle.id).first(),
        },
    )
