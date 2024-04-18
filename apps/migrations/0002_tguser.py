# Generated by Django 5.0.3 on 2024-04-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TgUser",
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
                (
                    "username",
                    models.CharField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]