# Generated by Django 5.1.5 on 2025-01-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0003_dips_rank_pull_ups_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dips',
            name='rank',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
