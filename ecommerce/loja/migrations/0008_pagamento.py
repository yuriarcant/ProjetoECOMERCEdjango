# Generated by Django 5.0.7 on 2024-10-30 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loja", "0007_tipo_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pagamento",
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
                ("id_pagamento", models.CharField(max_length=400)),
                (
                    "pedido",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="loja.pedido",
                    ),
                ),
            ],
        ),
    ]
