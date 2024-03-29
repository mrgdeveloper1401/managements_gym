# Generated by Django 5.0.1 on 2024-01-30 15:25

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodybuilders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodybuilding',
            name='insurance_end_date',
            field=django_jalali.db.models.jDateField(blank=True, help_text='If you have insured yourself, fill in this date // end date', null=True),
        ),
        migrations.AddField(
            model_name='bodybuilding',
            name='insurance_start_date',
            field=django_jalali.db.models.jDateField(blank=True, help_text='If you have insured yourself, fill in this date // start date', null=True),
        ),
        migrations.AlterField(
            model_name='bodybuilding',
            name='is_insurance',
            field=models.BooleanField(default=False, help_text='if insurance is true please complete start date and end date'),
        ),
    ]
