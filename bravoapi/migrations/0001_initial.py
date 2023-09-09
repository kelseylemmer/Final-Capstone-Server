# Generated by Django 4.2.4 on 2023-09-09 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('synopsis', models.CharField(max_length=1000)),
                ('runtime', models.DurationField()),
                ('episode', models.IntegerField()),
                ('air_date', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=70)),
                ('abbreviation', models.CharField(max_length=10)),
                ('series_premier', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=1000)),
                ('picture', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_number', models.IntegerField()),
                ('premier_date', models.CharField(max_length=10)),
                ('franchise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='bravoapi.franchise')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileEpisode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bravoapi.episode')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bravoapi.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='episodes',
            field=models.ManyToManyField(through='bravoapi.ProfileEpisode', to='bravoapi.episode'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='bravoapi.season'),
        ),
    ]
