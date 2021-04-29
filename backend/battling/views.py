from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from battling.forms import CreatorForm, OpponentForm
from battling.models import Battle
from pokemon.models import Pokemon
from services.battles import run_battle_and_send_email


class Home(TemplateView):
    template_name = "battling/home.html"


class Invite(TemplateView):
    template_name = "battling/invite.html"


class Opponent(TemplateView):  # will become an email
    template_name = "battling/opponent.html"


class BattleEnd(TemplateView):
    template_name = "battling/battle_end.html"


class CreateBattle(CreateView):
    model = Battle
    form_class = CreatorForm
    template_name = "battling/create_battle.html"
    success_url = reverse_lazy("invite")

    def form_valid(self, form):
        pokemon = form.cleaned_data

        form.instance.pokemon_1 = pokemon["creator_pokemon_1"]
        form.instance.pokemon_2 = pokemon["creator_pokemon_2"]
        form.instance.pokemon_3 = pokemon["creator_pokemon_3"]

        form.instance.save()

        return super().form_valid(form)


class EnterBattle(UpdateView):
    model = Battle
    form_class = OpponentForm
    template_name = "battling/enter_battle.html"
    success_url = reverse_lazy("battle_end")

    # def get_object(self):
    #     id_ = Battle.objects.latest("id").id
    #     return get_object_or_404(Battle, id=id_)

    def form_valid(self, form):
        pokemon = form.cleaned_data

        form.instance.pokemon_1 = pokemon["opponent_pokemon_1"]
        form.instance.pokemon_2 = pokemon["opponent_pokemon_2"]
        form.instance.pokemon_3 = pokemon["opponent_pokemon_3"]

        form.instance.save()
        id_ = Battle.objects.latest("id").id

        form.instance.battle_id = get_object_or_404(Battle, id=id_)
        run_battle_and_send_email(form.instance.battle_id.id)

        form.instance.battle_id.save()

        return super().form_valid(form)


def battle_details(request):
    battle_id = Battle.objects.latest("id")
    battle_info = Battle.objects.filter(id=battle_id.id).values()[0]

    # get the pokemons ids from the battles
    creator_pokemons_id = [battle_info["creator_pokemon_" + str(i) + "_id"] for i in range(1, 4)]
    opponent_pokemons_id = [battle_info["opponent_pokemon_" + str(i) + "_id"] for i in range(1, 4)]

    # get the pokemons from the DB
    creator_pokemon_list = [Pokemon.objects.filter(id=j).values()[0] for j in creator_pokemons_id]
    opponent_pokemon_list = [Pokemon.objects.filter(id=j).values()[0] for j in opponent_pokemons_id]

    return render(
        request,
        "battling/battle_details.html",
        {
            "winner": "jaja",  # battle_id.winner.email.split("@")[0],
            "creator": battle_id.creator.email.split("@")[0],
            "opponent": battle_id.opponent.email.split("@")[0],
            "creator_pkms": creator_pokemon_list,
            "opponent_pkms": opponent_pokemon_list,
        },
    )
