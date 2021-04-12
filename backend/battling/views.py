from django.shortcuts import redirect, render

from .battles.battle import battle
from .battles.email import send_battle_result
from .forms import RoundForm, RoundForm2
from .models import Battle
from .pokemons.pokemon_data import check_valid_team1, check_valid_team2, get_pokemon_from_api


def home(request):
    return render(request, "battling/home.html")


def battle_new(request):
    if request.method == "POST":
        form = RoundForm(request.POST)
        if form.is_valid():
            round_battle = form.save(commit=False)
            valid_team = check_valid_team1(round_battle)
            if valid_team:
                form.save(commit=False).save()
                return redirect("invite")
            message = "ERROR: your PKNs sum more than 600 points"
            return render(request, "battling/battle_new.html", {"form": form, "message": message})
    else:
        form = RoundForm()
    return render(request, "battling/battle_new.html", {"form": form})


def invite(request):
    return render(request, "battling/invite.html")


def opponent(request):
    return render(request, "battling/opponent.html")


def round_new2(request):
    battle_info = Battle.objects.latest("id")
    if request.method == "POST":
        form_round2 = RoundForm2(request.POST, instance=battle_info)
        if form_round2.is_valid():
            round_battle = form_round2.save(commit=False)
            valid_team = check_valid_team2(round_battle)
            if valid_team:
                form_round2.save()
                return redirect("battle_end")
            message = "ERROR: your PKNs sum more than 600 points"
            return render(
                request,
                "battling/round_new2.html",
                {"form_round2": form_round2, "battle": battle_info, "message": message},
            )
    else:
        form_round2 = RoundForm2()
    return render(
        request, "battling/round_new2.html", {"form_round2": form_round2, "battle": battle_info}
    )


def battle_end(request):
    battle_id = Battle.objects.latest("id")
    battle_info = Battle.objects.filter(id=battle_id.id).values()[0]

    creator_pkms = [get_pokemon_from_api(battle_info["pk1" + str(i)]) for i in range(1, 4)]
    opponent_pkms = [get_pokemon_from_api(battle_info["pk2" + str(i)]) for i in range(1, 4)]

    score = battle(creator_pkms, opponent_pkms)

    winner = (
        battle_id.player1.email if score["creator"] > score["opponent"] else battle_id.player2.email
    )
    send_battle_result(battle_id, winner, creator_pkms, opponent_pkms)

    return render(request, "battling/battle_end.html")


def fights(request):
    battle_id = Battle.objects.latest("id")
    battle_info = Battle.objects.filter(id=battle_id.id).values()[0]

    creator_pkms = [get_pokemon_from_api(battle_info["pk1" + str(i)]) for i in range(1, 4)]
    opponent_pkms = [get_pokemon_from_api(battle_info["pk2" + str(i)]) for i in range(1, 4)]

    score = battle(creator_pkms, opponent_pkms)

    winner = (
        battle_id.player1.email if score["creator"] > score["opponent"] else battle_id.player2.email
    )

    return render(
        request,
        "battling/fights.html",
        {
            "winner": winner,
            "creator_pkms": creator_pkms,
            "opponent_pkms": opponent_pkms,
        },
    )
