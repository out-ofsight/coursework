# Generated by Django 3.1.2 on 2020-11-19 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start_menu', '0007_auto_20201119_0827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='id_of_publish_house',
            new_name='id_of_publish_house_id',
        ),
    ]