from django.db import models


# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=200)
    description = models. CharField(max_length=1000)
    director = models.CharField(max_length=200)
    release_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    picture = models.ImageField(upload_to = 'static/media')
    date_modified = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['director',]

class Website(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()
    owner = models.CharField(max_length=200)
    logo = models.ImageField()
    date_modified = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ['owner',]

class Breeds(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    is_official = models.CharField(max_length=200)
    date_modified = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return'{}'.format(self.description)
