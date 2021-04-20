# Generated by Django 3.1.7 on 2021-04-20 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('c_pokemon_1', models.CharField(max_length=200, null=True, verbose_name='Pokemon 1:')),
                ('c_pokemon_2', models.CharField(max_length=200, null=True, verbose_name='Pokemon 2:')),
                ('c_pokemon_3', models.CharField(max_length=200, null=True, verbose_name='Pokemon 3:')),
                ('o_pokemon_1', models.CharField(max_length=200, null=True, verbose_name='Pokemon 1:')),
                ('o_pokemon_2', models.CharField(max_length=200, null=True, verbose_name='Pokemon 2:')),
                ('o_pokemon_3', models.CharField(max_length=200, null=True, verbose_name='Pokemon 3:')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='You are:')),
                ('opponent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Opponent:')),
            ],
        ),
    ]
