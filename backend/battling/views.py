from django.shortcuts import render
from django.shortcuts import redirect
from users.models import User
from .models import Battle
from .forms import RoundForm, RoundForm2
from urllib.parse import urljoin
from django.conf import settings
import requests
from .battles.battle import round



# Create your views here.
def home(request):
    gamer = Battle.objects.all()
    return render(request, 'battling/home.html', { 'gamer' : gamer})

def get_pokemon_from_api(poke_name):
    url = urljoin(settings.POKE_API_URL, poke_name)
    response = requests.get(url)
    data = response.json()
    info = {
        "poke_id": data["id"],
        "name": data["name"],
        "defense": data["stats"][3]["base_stat"],
        "attack": data["stats"][4]["base_stat"],
        "hp": data["stats"][5]["base_stat"],
    }
    return info


def sumValid(pokemon):
    sumResult = pokemon["attack"] +  pokemon["defense"] + pokemon["hp"]
    return sumResult

def battle_new(request):
    if request.method == "POST":
        form = RoundForm(request.POST)
        if form.is_valid():
            battle = form.save(commit=False)
            dataPK11 = get_pokemon_from_api(battle.pk11)
            dataPK12 = get_pokemon_from_api(battle.pk12)
            dataPK13 = get_pokemon_from_api(battle.pk13)
            sumPK11 = sumValid(dataPK11)
            sumPK12 = sumValid(dataPK12)
            sumPK13 = sumValid(dataPK13)
            sumAll = sumPK11 + sumPK12 + sumPK13
            if (sumAll <= 600):
                battle.save()
                return redirect('invite')
            if (sumAll > 600):
                message = "ERROR: The PKNs you selected sum more than 600 points, please choose again"
                return render(request, 'battling/battle_new.html', {'form': form, 'message': message})
    else:
        form = RoundForm()
    return render(request, 'battling/battle_new.html', {'form': form})

def invite(request):
    return render(request, 'battling/invite.html')

def opponent(request):
    return render(request, 'battling/opponent.html')

def round_new2(request):
    battleInfo = Battle.objects.get(id=72)
    if request.method == "POST":
        formRound2 = RoundForm2(request.POST, instance=battleInfo)
        if formRound2.is_valid():
            teste = formRound2.save(commit=False)
            dataPK21 = get_pokemon_from_api(teste.pk21)
            dataPK22 = get_pokemon_from_api(teste.pk22)
            dataPK23 = get_pokemon_from_api(teste.pk23)
            sumPK21 = sumValid(dataPK21)
            sumPK22 = sumValid(dataPK22)
            sumPK23 = sumValid(dataPK23)
            sumAll = sumPK21 + sumPK22 + sumPK23
            if (sumAll <= 600):
                formRound2.save()
                return redirect('home')
            if (sumAll > 600):
                message = "ERROR: The PKNs you selected sum more than 600 points, please choose again"
                return render(request, 'battling/round_new2.html', {'formRound2': formRound2, 'battle':battleInfo, 'message': message})
    else:
        formRound2 = RoundForm2()
    return render(request, 'battling/round_new2.html', {'formRound2': formRound2, 'battle':battleInfo})

def batalha(request):
    team1 = []
    team2 = []
    battle_info = Battle.objects.filter(id=65).values()[0]
    points = {'player1': 0, 'player2': 0}
    for i in range(1,4):
        team1.append(get_pokemon_from_api(battle_info['pk1'+str(i)])["name"])
        pokemon_c_atk = get_pokemon_from_api(battle_info['pk1'+str(i)])["attack"]
        pokemon_c_def = get_pokemon_from_api(battle_info['pk1'+str(i)])["defense"]
        pokemon_c_hp = get_pokemon_from_api(battle_info['pk1'+str(i)])["hp"]

        team2.append(get_pokemon_from_api(battle_info['pk2'+str(i)])["name"])
        pokemon_o_atk = get_pokemon_from_api(battle_info['pk2'+str(i)])["attack"]
        pokemon_o_def = get_pokemon_from_api(battle_info['pk2'+str(i)])["defense"]
        pokemon_o_hp = get_pokemon_from_api(battle_info['pk2'+str(i)])["hp"]

        points = round(pokemon_c_atk, pokemon_c_def, pokemon_c_hp, pokemon_o_atk, pokemon_o_def, pokemon_o_hp, points)

    if points['player1'] > points['player2']:
        winner = "Player1 won!"
    else:
        winner = "Player2 won!"

    return render(request, 'battling/batalha.html', { 'team1': team1, 'team2': team2, 'winner' : winner})
