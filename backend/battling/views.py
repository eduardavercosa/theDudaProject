from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from battling.forms import CreatorForm, OpponentForm
from battling.models import Battle
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

    def get_battle(self):
        id_ = Battle.objects.last().id
        return get_object_or_404(Battle, id=id_)

    def form_valid(self, form):
        pokemon = form.cleaned_data

        form.instance.pokemon_1 = pokemon["opponent_pokemon_1"]
        form.instance.pokemon_2 = pokemon["opponent_pokemon_2"]
        form.instance.pokemon_3 = pokemon["opponent_pokemon_3"]

        form.instance.save()

        form.instance.battle_id = self.get_battle().id
        run_battle_and_send_email(form.instance.battle_id)

        return super().form_valid(form)


# Had to change it, otherwise it wouldn't commit! But it's not ready
class DetailBattle(TemplateView):
    template_name = "battling/battle_details.html"
