# Generated by Django 5.0 on 2023-12-07 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commercial_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commercialproperty',
            old_name='address',
            new_name='address1',
        ),
    ]
