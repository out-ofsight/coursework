from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver


class Publishing_House(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название издательства')
    location = models.CharField(max_length=50, verbose_name='Локация')
    
    def __str__(self):
        return self.name

class Serie(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя серии')
    is_ended = models.BooleanField(verbose_name='Законченость серии')
    description = models.TextField(max_length=300, verbose_name='Описание')
    
    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    information_about = models.TextField(max_length=300)
    birth_date = models.DateField()
    death_date = models.DateField()
    def __str__(self):
        return self.name

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
    cover_image = models.ImageField(default='default_book_cover.jpg', upload_to='cover_books')
    description = models.TextField(max_length=300)
    book_text_path = models.FileField(blank=True, upload_to='books')
    year_of_wrote = models.DateField()
    year_of_publishing = models.DateField()
    id_of_publish_house = models.ForeignKey(Publishing_House, on_delete=models.PROTECT)
    id_of_series = models.ForeignKey(Serie, on_delete=models.PROTECT)
    service_book = models.ManyToManyField(Service)
    genre_book = models.ManyToManyField(Genre)
    language_book = models.ManyToManyField(Language)
    author_book = models.ManyToManyField(Author)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)

        img = Image.open(self.cover_image.path)

        if img.height > 400 or img.width > 300:
            output_size = (400, 300)
            img.thumbnail(output_size)
            img.save(self.cover_image.path)


class User_Library(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)

