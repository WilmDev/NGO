# Generated by Django 2.1.3 on 2018-11-30 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20181129_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_end_date',
            field=models.DateField(),
        ),
    ]
