# Generated by Django 5.1.5 on 2025-01-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pull_ups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Score_dips',
        ),
        migrations.DeleteModel(
            name='Score_pull_ups',
        ),
    ]
