# Generated by Django 2.1.3 on 2018-11-30 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20181129_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='registration_open',
            new_name='event_requested',
        ),
    ]