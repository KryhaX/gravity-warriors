# Generated by Django 5.1.5 on 2025-01-16 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score_dips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('dips', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score_pull_ups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('pull_ups', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
