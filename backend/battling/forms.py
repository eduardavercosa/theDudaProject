from django import forms

from .models import Battle


class CreatorForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = ("creator", "opponent", "c_pokemon_1", "c_pokemon_2", "c_pokemon_3")


class OpponentForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = ("o_pokemon_1", "o_pokemon_2", "o_pokemon_3")
