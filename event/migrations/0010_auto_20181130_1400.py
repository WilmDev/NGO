# Generated by Django 2.1.3 on 2018-11-30 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20181130_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_requested',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
