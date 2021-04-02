from django.shortcuts import render
from django.shortcuts import redirect
from urllib.parse import urljoin
import requests
from .models import Battle
from .forms import RoundForm, RoundForm2
from django.conf import settings
from .battles.battle import round


def home(request):
    gamer = Battle.objects.all()
    return render(request, 'battling/home.html', {'gamer': gamer})


def get_pokemon_from_api(poke_name):
    url = urljoin(settings.POKE_API_URL, poke_name.lower())
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
    sum_result = pokemon["attack"] + pokemon["defense"] + pokemon["hp"]
    return sum_result


def battle_new(request):
    if request.method == "POST":
        form = RoundForm(request.POST)
        if form.is_valid():
            battle = form.save(commit=False)
            data_pk11 = get_pokemon_from_api(battle.pk11)
            data_pk12 = get_pokemon_from_api(battle.pk12)
            data_pk13 = get_pokemon_from_api(battle.pk13)
            sum_pk11 = sumValid(data_pk11)
            sum_pk12 = sumValid(data_pk12)
            sum_pk13 = sumValid(data_pk13)
            sum_all = sum_pk11 + sum_pk12 + sum_pk13
            if sum_all <= 600:
                battle.save()
                return redirect('invite')
            if sum_all > 600:
                message = "ERROR: The PKNs sum more than 600 pts. Please choose again"
                return render(request, 'battling/battle_new.html', {'form': form,
                                                                    'message': message})
    else:
        form = RoundForm()
    return render(request, 'battling/battle_new.html', {'form': form})


def invite(request):
    return render(request, 'battling/invite.html')


def opponent(request):
    return render(request, 'battling/opponent.html')


def round_new2(request):
    battle_info = Battle.objects.latest('id')
    if request.method == "POST":
        form_round2 = RoundForm2(request.POST, instance=battle_info)
        if form_round2.is_valid():
            teste = form_round2.save(commit=False)
            data_pk21 = get_pokemon_from_api(teste.pk21)
            data_pk22 = get_pokemon_from_api(teste.pk22)
            data_pk23 = get_pokemon_from_api(teste.pk23)
            sum_pk21 = sumValid(data_pk21)
            sum_pk22 = sumValid(data_pk22)
            sum_pk23 = sumValid(data_pk23)
            sum_all = sum_pk21 + sum_pk22 + sum_pk23
            if sum_all <= 600:
                form_round2.save()
                return redirect('home')
            if sum_all > 600:
                message = "ERROR: The PKNs sum more than 600 pts. Please choose again"
                return render(request, 'battling/round_new2.html', {'form_round2': form_round2,
                                                                    'battle': battle_info,
                                                                    'message': message})
    else:
        form_round2 = RoundForm2()
    return render(request, 'battling/round_new2.html', {'form_round2': form_round2,
                                                        'battle': battle_info})

def fights(request):
    team1 = []
    team2 = []
    id_info = Battle.objects.latest('id')
    battle_info = Battle.objects.filter(id=id_info.id).values()[0]
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
        winner = "Creator won!"
    else:
        winner = "Opponent won!"

    return render(request, 'battling/fights.html', { 'team1': team1, 'team2': team2, 'winner' : winner})
