# Generated by Django 4.1.5 on 2023-01-20 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artiste",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=140)),
                (
                    "style",
                    models.CharField(
                        choices=[
                            ("POP", "pop"),
                            ("RAP", "rap"),
                            ("CLASSIC", "classic"),
                            ("ROCK", "rock"),
                            ("UNDEFINED", "undefined"),
                        ],
                        max_length=60,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Chanson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titre", models.CharField(max_length=140)),
                ("durée", models.FloatField(max_length=140)),
                ("date", models.DateTimeField()),
                (
                    "artiste",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="music.artiste"
                    ),
                ),
            ],
        ),
    ]
