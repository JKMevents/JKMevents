# Generated by Django 4.2.4 on 2024-01-26 17:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0004_ticketcounter"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Member",
        ),
        migrations.DeleteModel(
            name="ticket",
        ),
    ]
