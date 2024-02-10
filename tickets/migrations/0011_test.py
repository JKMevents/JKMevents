# Generated by Django 4.1.12 on 2024-02-01 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0010_remove_user_information_user_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="test",
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
                ("count", models.IntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tickets.user_information",
                    ),
                ),
            ],
        ),
    ]
