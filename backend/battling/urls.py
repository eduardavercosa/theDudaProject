from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('battle/new/', views.battle_new, name='battle_new'),
    path('invite/', views.invite, name='invite'),
    path('opponent/', views.opponent, name='opponent'),
    path('opponent/round', views.round_new2, name='round_new2'),
]
