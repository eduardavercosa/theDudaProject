from django.urls import path

from battling.views import CreateBattle, EnterBattle, Home, Invite, Opponent

from . import views


urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path("create_battle", CreateBattle.as_view(), name="CreateBattle"),
    path("invite/", Invite.as_view(), name="Invite"),
    path("opponent/", Opponent.as_view(), name="Opponent"),
    path("enter_battle", EnterBattle.as_view(), name="EnterBattle"),
    path("winner/", views.fights, name="fights"),
    path("battle_end/", views.battle_end, name="battle_end"),
]
