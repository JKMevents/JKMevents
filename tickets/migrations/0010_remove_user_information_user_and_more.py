# Generated by Django 4.1.12 on 2024-02-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0009_delete_ticket"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user_information",
            name="user",
        ),
        migrations.AddField(
            model_name="user_information",
            name="username",
            field=models.CharField(default="default_username", max_length=254),
        ),
        migrations.AlterField(
            model_name="user_information",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
