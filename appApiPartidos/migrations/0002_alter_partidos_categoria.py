# Generated by Django 5.1.4 on 2024-12-18 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appApiPartidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partidos',
            name='categoria',
            field=models.CharField(choices=[('primera A', 'Primera A'), ('primera B', 'Primera B'), ('copa Bet Play', 'Copa Bet Play')], max_length=100),
        ),
    ]
