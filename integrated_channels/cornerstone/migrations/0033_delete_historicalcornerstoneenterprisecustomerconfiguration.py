# Generated by Django 3.2.19 on 2024-02-20 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0032_delete_cornerstoneapirequestlogs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalCornerstoneEnterpriseCustomerConfiguration',
        ),
    ]