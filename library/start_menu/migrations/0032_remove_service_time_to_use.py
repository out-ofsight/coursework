# Generated by Django 3.1.4 on 2021-01-10 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start_menu', '0031_auto_20210110_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='time_to_use',
        ),
    ]