from django.db import models
from django.contrib.auth.models import User

class Publishing_House(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

class Serie(models.Model):
    name = models.CharField(max_length=50)
    is_ended = models.BooleanField()
    description = models.TextField(max_length=300)
    
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
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    time_to_use = models.DateField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    server_connection_date = models.DateField(null=True, blank=True)

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



