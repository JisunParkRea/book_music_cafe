from django.db import models

class MusicRank1(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    cover_img = models.CharField(max_length=100)