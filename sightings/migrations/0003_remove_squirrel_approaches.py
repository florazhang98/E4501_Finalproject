# Generated by Django 3.0.7 on 2020-10-21 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0002_auto_20201021_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squirrel',
            name='Approaches',
        ),
    ]