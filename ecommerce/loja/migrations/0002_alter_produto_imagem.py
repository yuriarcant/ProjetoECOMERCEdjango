# Generated by Django 5.0.7 on 2024-08-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loja", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
