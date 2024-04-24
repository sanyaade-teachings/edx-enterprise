# Generated by Django 3.2.23 on 2024-04-23 12:26

from django.db import migrations


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
        ('blackboard', '0022_blackboardglobalconfiguration_decrypted_app_secret'),
    ]

    operations = [
        migrations.RunPython(populate_decrypted_fields, reverse_code=migrations.RunPython.noop),
    ]