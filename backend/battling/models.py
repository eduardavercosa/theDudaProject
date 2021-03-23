from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms
from pokemons.models import Pokemon

class Battle(models.Model):
    player1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='player1', verbose_name='What is your name?')
    player2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='player2_gamer', verbose_name='Choose your opponent:')

    pk11 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pk11', verbose_name='Pokemon 1:')
    pk21 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pk21', verbose_name='Pokemon 2:')
    pk31 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pk31', verbose_name='Pokemon 3:')

    pk12 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pk12', verbose_name='Pokemon 1:')
    pk22 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pk22', verbose_name='Pokemon 2:')
    pk32 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pk32', verbose_name='Pokemon 3:')

    #winner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='winner_gamer', null=True)

    def publish(self):
        self.save()


'''
class Round(models.Model):
    #status = models.ForeignKey(settings.STATUS_MODEL, on_delete=models.CASCADE)
    winner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='winner_gamer_round', null=True)
    id_batalha = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='batalha_id', null=True)
    pk11 = models.CharField(max_length=200, verbose_name='Pokemon 1:', null=True)
    pk21 = models.CharField(max_length=200, verbose_name='Pokemon 2:', null=True)
    pk31 = models.CharField(max_length=200, verbose_name='Pokemon 3:', null=True)
'''
