from django.conf import settings
from django.db import models
from urllib.parse import urljoin
import requests

class Gamer(models.Model):
    name = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name



class Battle(models.Model):
    url = urljoin(settings.POKE_API_URL, "?limit=1000")
    response = requests.get(url)
    data = response.json()

    id = models.AutoField(primary_key=True)
    player1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+', verbose_name='You are:',  null=True)
    player2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+', verbose_name='Opponent:',  null=True)
    pk11 = models.CharField(max_length=200, verbose_name='Pokemon 1:', null=True)
    pk21 = models.CharField(max_length=200, verbose_name='Pokemon 2:', null=True)
    pk31 = models.CharField(max_length=200, verbose_name='Pokemon 3:', null=True)
    pk12 = models.CharField(max_length=200, verbose_name='Pokemon 1:', null=True)
    pk22 = models.CharField(max_length=200, verbose_name='Pokemon 2:', null=True)
    pk32 = models.CharField(max_length=200, verbose_name='Pokemon 3:', null=True)
    def publish(self):
        self.save()


class Status(models.Model):
    sequence = models.IntegerField()

    def publish(self):
        self.save()
