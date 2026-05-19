from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='название жанра')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    poster = models.ImageField(upload_to='posters/')
    actors = models.CharField(max_length=200, verbose_name='актеры')
    release_date = models.DateField(verbose_name='дата релиза')
    duration = models.PositiveIntegerField(verbose_name='длительность в минутах')
    country = models.CharField(max_length=100, verbose_name='страна')
    language = models.CharField(max_length=100, verbose_name='язык')
    budget = models.PositiveIntegerField(verbose_name='бюджет')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    genres = models.ManyToManyField(Genre, verbose_name='жанр')

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    text = models.TextField(verbose_name='комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text



class VIPBooking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь')
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, verbose_name='фильм')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата брони')

    def __str__(self):
        return f'{self.user} Забронировано длч вип клиента {self.movie}'