# Generated by Django 4.2.1 on 2023-12-01 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dune', '0007_tagpost_alter_dune_cat_dune_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('affiliation', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='dune',
            name='planet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='character', to='dune.planet'),
        ),
    ]