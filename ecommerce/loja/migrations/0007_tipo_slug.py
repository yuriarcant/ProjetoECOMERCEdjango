# Generated by Django 5.0.7 on 2024-09-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loja", "0006_categoria_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="tipo",
            name="slug",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
