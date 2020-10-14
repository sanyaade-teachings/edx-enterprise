# Generated by Django 2.2.16 on 2020-10-14 20:01

from django.db import migrations, models
import enterprise.validators


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0114_alter_customer_branding_configuration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enterprisecustomerbrandingconfiguration',
            old_name='primary_color',
            new_name='_primary_color',
        ),
        migrations.RenameField(
            model_name='enterprisecustomerbrandingconfiguration',
            old_name='secondary_color',
            new_name='_secondary_color',
        ),
        migrations.RenameField(
            model_name='enterprisecustomerbrandingconfiguration',
            old_name='tertiary_color',
            new_name='_tertiary_color',
        ),
        migrations.AlterField(
            model_name='enterprisecustomerbrandingconfiguration',
            name='_primary_color',
            field=models.CharField(blank=True, db_column='primary_color', max_length=7, null=True, validators=[enterprise.validators.validate_hex_color]),
        ),
        migrations.AlterField(
            model_name='enterprisecustomerbrandingconfiguration',
            name='_secondary_color',
            field=models.CharField(blank=True, db_column='secondary_color', max_length=7, null=True, validators=[enterprise.validators.validate_hex_color]),
        ),
        migrations.AlterField(
            model_name='enterprisecustomerbrandingconfiguration',
            name='_tertiary_color',
            field=models.CharField(blank=True, db_column='tertiary_color', max_length=7, null=True, validators=[enterprise.validators.validate_hex_color]),
        ),
    ]