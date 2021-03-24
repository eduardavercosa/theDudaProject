from django.shortcuts import render
from django.shortcuts import redirect
from users.models import User
from .models import Battle
from .forms import BattleForm, RoundForm, RoundForm2


# Create your views here.
def home(request):
    gamer = Battle.objects.all()
    return render(request, 'battling/home.html', { 'gamer' : gamer})

def battle_new(request):
    if request.method == "POST":
        form = BattleForm(request.POST)
        if form.is_valid():
            battle = form.save(commit=False)
            battle.save()
            return redirect('round_new')
    else:
        form = BattleForm()
    return render(request, 'battling/battle_new.html', {'form': form})

def round_new(request):
    # if request.method == "POST":
    #     formRound = RoundForm(request.POST)
    #     if formRound.is_valid():
    #         roundBattle = formRound.save(commit=False)
    #         roundBattle.save()
    #         return redirect('home')
    # else:
    #     formRound = RoundForm()
    return render(request, 'battling/round_new.html')

def invite(request):
    return render(request, 'battling/invite.html')

def opponent(request):
    return render(request, 'battling/opponent.html')

def round_new2(request):
    battleInfo = Battle.objects.get(id=9)
    if request.method == "POST":
        formRound2 = RoundForm2(request.POST, instance=battleInfo)
        if formRound2.is_valid():
            formRound2.save()
            return redirect('home')
    else:
        formRound2 = RoundForm2()
    return render(request, 'battling/round_new2.html', {'formRound2': formRound2, 'battleInfo': battleInfo})
