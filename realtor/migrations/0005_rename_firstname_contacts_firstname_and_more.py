# Generated by Django 4.0 on 2022-11-05 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0004_rename_owner_forsale_ownerid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='firstname',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='contacts',
            old_name='lastname',
            new_name='lastName',
        ),
    ]
