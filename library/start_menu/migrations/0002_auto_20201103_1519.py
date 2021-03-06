# Generated by Django 3.1.2 on 2020-11-03 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('start_menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('information_about', models.TextField(max_length=300)),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Author_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start_menu.author')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('page_count', models.BigIntegerField()),
                ('cover_image_path', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('book_text_path', models.CharField(max_length=100)),
                ('year_of_wrote', models.DateField()),
                ('year_of_publishing', models.DateField()),
                ('id_of_publish_house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start_menu.publishing_house')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Genre_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start_menu.book')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start_menu.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Language_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start_menu.book')),
                ('language_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start_menu.language')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('time_to_use', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Service_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start_menu.book')),
                ('servise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start_menu.service')),
            ],
        ),
        migrations.CreateModel(
            name='User_Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start_menu.book')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.RenameModel(
            old_name='Series',
            new_name='Serie',
        ),
        migrations.AddField(
            model_name='book',
            name='id_of_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start_menu.serie'),
        ),
        migrations.AddField(
            model_name='author_book',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start_menu.book'),
        ),
    ]
