from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from . import validators


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('by_category', kwargs={'cat_id': self.pk})


class Film(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    about = models.CharField(max_length=255, verbose_name="Информация")
    image = models.ImageField(upload_to=f'images/', null=True, verbose_name="Обложка")
    video = models.FileField(upload_to=f'videos/', validators=[validators.validate_file_extension], null=True, verbose_name="Видеофайл")
    author = models.CharField(max_length=100, null=True, verbose_name="Автор")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'film_id': self.pk})


class UserFilmRelation(models.Model):
    RATE = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Cool'),
        (5, 'Very Good')
    )

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    video = models.ForeignKey(Film, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE)
    in_bookmarks = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} : {self.rate}"



