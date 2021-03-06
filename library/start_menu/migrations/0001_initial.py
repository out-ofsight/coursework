# Generated by Django 3.1.2 on 2020-11-03 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('page_count', models.BigIntegerField()),
                ('cover_image_path', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('book_text_path', models.CharField(max_length=100)),
                ('year_of_wrote', models.DateField()),
                ('year_of_publishing', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Publishing_House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_ended', models.BooleanField()),
                ('description', models.TextField(max_length=300)),
            ],
        ),
    ]
