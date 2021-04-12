from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .battles.battle import battle
from .battles.email import send_battle_result
from .forms import CreatorForm, OpponentForm
from .models import Battle
from .pokemons.pokemon_data import get_pokemon_from_api, valid_team


class Home(TemplateView):
    template_name = "home.html"


class Invite(TemplateView):
    template_name = "invite.html"


class Opponent(TemplateView):  # will become an email
    template_name = "opponent.html"


class CreateBattle(CreateView):
    model = Battle
    form_class = CreatorForm
    template_name = "create_battle.html"

    def get_c(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post_c(self, request):
        battle_field = self.model.objects.latest("id")
        form = self.form_class(request.POST, instance=battle_field)
        if form.is_valid():
            round_battle = form.save(commit=False)
            c_team = valid_team(round_battle, "c")
            if c_team:
                form.save()
                return redirect("Invite")
            message = "ERROR: you selected sum more than 600 points"
            return render(
                request, self.template_name, {"form": self.form_class, "message": message}
            )
        return self.get(request)


class EnterBattle(CreateView):
    model = Battle
    form_class = OpponentForm
    template_name = "enter_battle.html"

    def get_o(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post_o(self, request):
        battle_field = self.model.objects.latest("id")
        form = self.form_class(request.POST, instance=battle_field)
        if form.is_valid():
            round_battle = form.save(commit=False)
            o_team = valid_team(round_battle, "o")
            if o_team:
                form.save()
                return redirect("battle_end")
            message = "ERROR: you selected sum more than 600 points"
            return render(
                request, self.template_name, {"form": self.form_class, "message": message}
            )
        return self.get(request)


def battle_end(request):
    battle_id = Battle.objects.latest("id")
    battle_info = Battle.objects.filter(id=battle_id.id).values()[0]

    creator_pkms = [get_pokemon_from_api(battle_info["c_pokemon_" + str(i)]) for i in range(1, 4)]
    opponent_pkms = [get_pokemon_from_api(battle_info["o_pokemon_" + str(i)]) for i in range(1, 4)]

    score = battle(creator_pkms, opponent_pkms)

    winner = (
        battle_id.creator.email
        if score["creator"] > score["opponent"]
        else battle_id.opponent.email
    )
    send_battle_result(battle_id, winner, creator_pkms, opponent_pkms)

    return render(request, "battling/battle_end.html")


def fights(request):
    battle_id = Battle.objects.latest("id")
    battle_info = Battle.objects.filter(id=battle_id.id).values()[0]

    creator_pkms = [get_pokemon_from_api(battle_info["c_pokemon" + str(i)]) for i in range(1, 4)]
    opponent_pkms = [get_pokemon_from_api(battle_info["o_pokemon" + str(i)]) for i in range(1, 4)]

    score = battle(creator_pkms, opponent_pkms)

    winner = (
        battle_id.creator.email
        if score["creator"] > score["opponent"]
        else battle_id.opponent.email
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
