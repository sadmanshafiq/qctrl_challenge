from django.db import models

# Create your models here.
class Control_Types(models.Model):
    control_types = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.control_types

class Controls(models.Model):

    name = models.CharField(max_length=250)
    ctype = models.ForeignKey(Control_Types, on_delete= models.PROTECT, blank=True, null=True)



def __str__(self):
    return "{} - {}".format(self.name, self.ctype)