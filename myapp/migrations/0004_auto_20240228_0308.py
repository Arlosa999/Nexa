# Generated by Django 3.2.8 on 2024-02-28 03:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_appointment_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='date_time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
