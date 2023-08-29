# Generated by Django 3.2.20 on 2023-08-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0180_chatgptresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomer',
            name='enable_generation_of_api_credentials',
            field=models.BooleanField(default=False, verbose_name='Allow generation of API credentials'),
        ),
        migrations.AddField(
            model_name='historicalenterprisecustomer',
            name='enable_generation_of_api_credentials',
            field=models.BooleanField(default=False, verbose_name='Allow generation of API credentials'),
        ),
    ]
