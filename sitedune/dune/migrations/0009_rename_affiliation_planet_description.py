# Generated by Django 4.2.1 on 2023-12-01 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dune', '0008_planet_dune_planet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planet',
            old_name='affiliation',
            new_name='description',
        ),
    ]