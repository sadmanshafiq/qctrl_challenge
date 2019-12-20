from django.db import models

# Create your models here.
class Controls(models.Model):
    name = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)

def __str__(self):
    return "{} - {}".format(self.name, self.artist)