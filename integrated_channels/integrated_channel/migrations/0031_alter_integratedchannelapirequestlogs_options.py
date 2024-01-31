# Generated by Django 3.2.22 on 2024-01-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrated_channel', '0030_integratedchannelapirequestlogs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='integratedchannelapirequestlogs',
            options={'verbose_name_plural': 'Integrated channels API request logs'},
        ),
        migrations.RemoveField(
            model_name='integratedchannelapirequestlogs',
            name='api_record',
        ),
        migrations.AddField(
            model_name='integratedchannelapirequestlogs',
            name='response_body',
            field=models.TextField(blank=True, help_text='API call response body', null=True),
        ),
        migrations.AddField(
            model_name='integratedchannelapirequestlogs',
            name='status_code',
            field=models.PositiveIntegerField(blank=True, help_text='API call response HTTP status code', null=True),
        ),
        migrations.AlterField(
            model_name='integratedchannelapirequestlogs',
            name='time_taken',
            field=models.FloatField(),
        ),
    ]
