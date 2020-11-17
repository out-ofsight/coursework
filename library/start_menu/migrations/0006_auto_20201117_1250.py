# Generated by Django 3.1.2 on 2020-11-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_menu', '0005_auto_20201110_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishing_house',
            name='location',
            field=models.CharField(max_length=50, verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='publishing_house',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название издательства'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='description',
            field=models.TextField(max_length=300, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='is_ended',
            field=models.BooleanField(verbose_name='Законченость серии'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя серии'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(max_length=300, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название сервиса'),
        ),
    ]