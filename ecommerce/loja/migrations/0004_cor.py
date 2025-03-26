# Generated by Django 5.0.7 on 2024-08-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loja", "0003_banner"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cor",
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
                ("nome", models.CharField(blank=True, max_length=200, null=True)),
                ("codigo", models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
