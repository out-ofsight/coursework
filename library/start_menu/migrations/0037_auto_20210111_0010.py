# Generated by Django 3.1.4 on 2021-01-11 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_menu', '0036_auto_20210110_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='time_to_use',
            field=models.IntegerField(),
        ),
    ]
