from django.db import models

# Create your models here.
class Controls(models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)

def __str__(self):
    return "{} - {}".format(self.title, self.artist)