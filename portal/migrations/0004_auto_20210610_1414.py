# Generated by Django 3.1.7 on 2021-06-10 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20210610_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='city',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='country',
            new_name='Country',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='country_code',
            new_name='Country_code',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='full_address',
            new_name='Full_address',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='latitude',
            new_name='Latitude',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='longitude',
            new_name='Longitude',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='postal_code',
            new_name='Postal_code',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='state',
            new_name='State',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='street_name',
            new_name='Street_name',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='street_number',
            new_name='Street_number',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='address',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='number',
            new_name='Number',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='address',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='company',
            new_name='Company',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='sitesettings',
            old_name='site',
            new_name='Site',
        ),
        migrations.RenameField(
            model_name='usersettings',
            old_name='user',
            new_name='User',
        ),
    ]
