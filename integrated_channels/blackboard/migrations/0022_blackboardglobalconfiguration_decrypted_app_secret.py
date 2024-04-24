# Generated by Django 3.2.23 on 2024-04-24 15:06

from django.db import migrations
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blackboard', '0021_auto_20240423_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='blackboardglobalconfiguration',
            name='decrypted_app_secret',
            field=fernet_fields.fields.EncryptedCharField(blank=True, default='', help_text='The application API secret used to make to identify ourselves as the edX integration app to customer instances. Called Application Secret in Blackboard', max_length=255, verbose_name='API Client Secret or Application Secret'),
        ),
    ]
