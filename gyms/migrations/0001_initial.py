# Generated by Django 5.0.1 on 2024-01-29 14:25

import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bodybuilders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('gym_name', models.CharField(max_length=100, unique=True)),
                ('en_gym_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('number_of_machine', models.PositiveSmallIntegerField(verbose_name='Number of machine')),
                ('is_active', models.BooleanField(default=False)),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gyms', to='bodybuilders.bodybuilding')),
            ],
            options={
                'verbose_name': 'gym',
                'verbose_name_plural': 'gyms',
                'db_table': 'gyms',
            },
        ),
        migrations.CreateModel(
            name='ContactGym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('mobile_phone', models.CharField(max_length=15, unique=True, verbose_name='mobile phone')),
                ('landing_phone', models.CharField(max_length=15, unique=True, verbose_name='landing phone')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('gym', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='contact_us_gym', to='gyms.gym')),
            ],
            options={
                'verbose_name': 'gym contact us',
                'verbose_name_plural': 'gym contact us',
                'db_table': 'gym_contact_us',
            },
        ),
        migrations.CreateModel(
            name='GymTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('male_opening_time', models.TimeField()),
                ('male_closing_time', models.TimeField()),
                ('female_opening_time', models.TimeField()),
                ('female_closing_time', models.TimeField()),
                ('explain_gym_time', models.TextField(blank=True, null=True, verbose_name='explain gym time')),
                ('is_active', models.BooleanField(default=True)),
                ('gym', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gym_time', to='gyms.gym')),
            ],
            options={
                'verbose_name': 'gym_time',
                'verbose_name_plural': 'gym times',
                'db_table': 'gym_time',
            },
        ),
        migrations.CreateModel(
            name='SocialNetworkClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('social_name', models.CharField(max_length=50, verbose_name='social name')),
                ('url_social', models.URLField()),
                ('is_active', models.BooleanField(default=True)),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_network_club', to='gyms.gym')),
            ],
            options={
                'verbose_name': 'social contact us',
                'verbose_name_plural': 'social contact us',
                'db_table': 'social_contact_us',
            },
        ),
    ]