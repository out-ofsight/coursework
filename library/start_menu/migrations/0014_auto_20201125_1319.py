# Generated by Django 3.1.2 on 2020-11-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_menu', '0013_auto_20201125_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_text_path',
            field=models.FileField(blank=True, upload_to='books'),
        ),
    ]
