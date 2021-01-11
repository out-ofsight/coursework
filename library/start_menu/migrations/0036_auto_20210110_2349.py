# Generated by Django 3.1.4 on 2021-01-10 23:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('start_menu', '0035_auto_20210110_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='time_to_use_in_days',
        ),
        migrations.AddField(
            model_name='service',
            name='time_to_use',
            field=models.DateField(default=datetime.datetime(2021, 1, 10, 23, 49, 49, 942587, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='server_connection_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
