# Generated by Django 3.2.20 on 2023-08-16 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('degreed2', '0023_alter_historicaldegreed2enterprisecustomerconfiguration_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaldegreed2enterprisecustomerconfiguration',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical degreed2 enterprise customer configuration'},
        ),
    ]