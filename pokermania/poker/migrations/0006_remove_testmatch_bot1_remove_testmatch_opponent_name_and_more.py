# Generated by Django 5.1 on 2025-02-27 01:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("poker", "0005_rename_opponent_wins_testmatch_total_rounds_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="testmatch",
            name="bot1",
        ),
        migrations.RemoveField(
            model_name="testmatch",
            name="opponent_name",
        ),
        migrations.RemoveField(
            model_name="testmatch",
            name="test_bot_wins",
        ),
        migrations.RemoveField(
            model_name="testmatch",
            name="total_chips_exchanged",
        ),
        migrations.RemoveField(
            model_name="testmatch",
            name="total_rounds",
        ),
        migrations.AddField(
            model_name="testmatch",
            name="players",
            field=models.ManyToManyField(
                related_name="test_matches", to="poker.testbot"
            ),
        ),
    ]
