# Generated by Django 3.1.7 on 2021-04-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poke_id', models.IntegerField(verbose_name='PokeAPI ID')),
                ('name', models.CharField(max_length=50)),
                ('img_url', models.CharField(blank=True, max_length=100)),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('hp', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Pokemon',
                'ordering': ('poke_id',),
            },
        ),
    ]
