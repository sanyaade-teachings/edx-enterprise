# Generated by Django 3.2.20 on 2023-08-16 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('degreed', '0031_alter_historicaldegreedenterprisecustomerconfiguration_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaldegreedenterprisecustomerconfiguration',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical degreed enterprise customer configuration'},
        ),
    ]