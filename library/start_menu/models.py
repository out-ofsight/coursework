from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver


class Publishing_House(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название издательства')
    location = models.CharField(max_length=50, verbose_name='Локация')


class Serie(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя серии')
    is_ended = models.BooleanField(verbose_name='Законченость серии')
    description = models.TextField(max_length=300, verbose_name='Описание')
    
    def __str__(self):
        return self.name, self.is_ended


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)


class Language(models.Model):
    name = models.CharField(max_length=50)


class Author(models.Model):
    name = models.CharField(max_length=50)
    information_about = models.TextField(max_length=300)
    birth_date = models.DateField()
    death_date = models.DateField()

class Service(models.Model):
    
        name = models.CharField(max_length=100, verbose_name='Название сервиса')
        description = models.TextField(max_length=300, verbose_name='Описание')
        time_to_use = models.DateField()
        
        def __str__(self):
            return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True)
    server_connection_date = models.DateField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Book(models.Model):
    name = models.CharField(max_length=100)
    page_count = models.BigIntegerField()
    cover_image_path = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    book_text_path = models.CharField(max_length=100)
    year_of_wrote = models.DateField()
    year_of_publishing = models.DateField()
    id_of_publish_house = models.ForeignKey(Publishing_House, on_delete=models.CASCADE)
    id_of_series = models.ForeignKey(Serie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User_Library(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Genre_Book(models.Model):
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)


class Language_Book(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)


class Author_Book(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)


class Service_Book(models.Model):
    servise_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
