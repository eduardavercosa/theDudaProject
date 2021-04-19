from django.urls import path

from battling.views import CreateBattle, EnterBattle, Home, Invite, Opponent

from . import views


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("create_battle", CreateBattle.as_view(), name="create_battle"),
    path("invite/", Invite.as_view(), name="invite"),
    path("opponent/", Opponent.as_view(), name="opponent"),
    path("enter_battle", EnterBattle.as_view(), name="enter_battle"),
    path("battle_end/", views.battle_end, name="battle_end"),
    path("battle_details/", views.battle_details, name="battle_details"),
]
