# Generated by Django 3.1.4 on 2021-01-10 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_menu', '0034_auto_20210110_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='time_to_use_in_days',
            field=models.BigIntegerField(default=0),
        ),
    ]
