from django.db import models

class BookRank1(models.Model):
    title = models.CharField(max_length=100)

class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    cover_img = models.CharField(max_length=100)
