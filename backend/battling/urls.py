from django.conf.urls import include, url  # noqa
from django.urls import path, include
from django.contrib import admin
from django.shortcuts import redirect
from common.views import homeView

import django_js_reverse.views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('battle/new/', views.battle_new, name='battle_new'),
    path('round/new/', views.round_new, name='round_new'),
    path('invite/', views.invite, name='invite'),
    path('opponent/', views.opponent, name='opponent'),
    path('opponent/round', views.round_new2, name='round_new2'),
]
