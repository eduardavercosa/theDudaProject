# Generated by Django 3.1.7 on 2021-04-12 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battling', '0005_auto_20210326_1549'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gamer',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]