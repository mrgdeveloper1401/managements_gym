# Generated by Django 5.0.1 on 2024-01-29 14:25

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernotification',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True),
        ),
    ]
