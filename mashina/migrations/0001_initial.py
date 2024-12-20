# Generated by Django 5.1.3 on 2024-11-25 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Haydovchi",
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
                ("ism", models.CharField(max_length=50)),
                ("familiya", models.CharField(max_length=50)),
                ("jshshir", models.CharField(max_length=14, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Mashina",
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
                ("raqam", models.CharField(max_length=15, unique=True)),
                ("nomi", models.CharField(max_length=50)),
                ("rangi", models.CharField(max_length=30)),
                ("ishlab_chiqarilgan_yili", models.PositiveIntegerField()),
                (
                    "haydovchi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mashinalar",
                        to="mashina.haydovchi",
                    ),
                ),
            ],
        ),
    ]
