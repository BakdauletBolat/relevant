from django.db import models


# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='brands/')

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.name


class TelegramUser(models.Model):
    chat_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)


class Project(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='projects/')
    short_description = models.TextField()
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='features/')
    short_description = models.TextField()
    icon_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.name


class Rating(models.Model):
    star = models.CharField(default="4", max_length=255)
    full_name = models.CharField(max_length=255)
    photo_user = models.ImageField(upload_to='photo-user/')
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

    def __str__(self):
        return self.full_name


class Request(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, verbose_name='Телефон номера')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, verbose_name='Телефон номера')
    photo = models.ImageField(upload_to='features/')
    instagram = models.CharField(max_length=255, verbose_name='Instagram')
    position = models.CharField(max_length=255, verbose_name='Должность')

    def __str__(self):
        return self.name
