# Generated by Django 3.2.20 on 2023-08-08 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('degreed', '0030_auto_20230719_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaldegreedenterprisecustomerconfiguration',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical degreed enterprise customer configuration', 'verbose_name_plural': 'historical degreed enterprise customer configurations'},
        ),
    ]
