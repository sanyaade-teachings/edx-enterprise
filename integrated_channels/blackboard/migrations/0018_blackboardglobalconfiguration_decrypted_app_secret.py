# Generated by Django 3.2.20 on 2023-10-11 09:48

from django.db import migrations
from integrated_channels.utils import dummy_reverse
import fernet_fields.fields


def populate_decrypted_fields(apps, schema_editor):
    """
    Populates the encryption fields with the data previously stored in database.
    """
    BlackboardGlobalConfiguration = apps.get_model('blackboard', 'BlackboardGlobalConfiguration')

    for blackboard_global_configuration in BlackboardGlobalConfiguration.objects.all():
        blackboard_global_configuration.decrypted_app_secret = blackboard_global_configuration.app_secret
        blackboard_global_configuration.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blackboard', '0017_alter_historicalblackboardenterprisecustomerconfiguration_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blackboardglobalconfiguration',
            name='decrypted_app_secret',
            field=fernet_fields.fields.EncryptedCharField(blank=True, default='', help_text='The application API secret used to make to identify ourselves as the edX integration app to customer instances. Called Application Secret in Blackboard', max_length=255, verbose_name='API Client Secret or Application Secret'),
        ),
        migrations.RunPython(populate_decrypted_fields, dummy_reverse),
    ]
