# Generated by Django 4.2.1 on 2023-11-12 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dune', '0005_category_dune_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dune',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dune.category'),
        ),
    ]
