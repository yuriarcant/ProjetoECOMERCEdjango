# Generated by Django 5.0.7 on 2024-09-11 19:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loja", "0005_alter_itemestoque_cor"),
    ]

    operations = [
        migrations.AddField(
            model_name="categoria",
            name="slug",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
