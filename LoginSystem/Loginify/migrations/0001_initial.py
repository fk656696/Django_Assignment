# Generated by Django 5.2 on 2025-04-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserDetails",
            fields=[
                (
                    "username",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(blank=True, max_length=12)),
            ],
        ),
    ]
