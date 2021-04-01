from django import forms
from .models import Battle


class RoundForm(forms.ModelForm):

    class Meta:
        model = Battle
        fields = ('player1', 'player2', 'pk11', 'pk12', 'pk13')


class RoundForm2(forms.ModelForm):

    class Meta:
        model = Battle
        fields = ('pk21', 'pk22', 'pk23')
