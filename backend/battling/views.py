from django.shortcuts import render
from django.shortcuts import redirect
from users.models import User
from .models import Battle
from .forms import RoundForm, RoundForm2
from urllib.parse import urljoin
from django.conf import settings
import requests
from .battles.battle import round


def home(request):
    gamer = Battle.objects.all()
    return render(request, 'battling/home.html', { 'gamer' : gamer})

