# models.py contains the fields that are being populated and placed focus on type
# as type needed to be valid, therefore used Choices to be sure of valid types

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

class Controls(models.Model):
    #Contains all the API parts, with choice explanation given

    #simple char field can be made unique if there was need to seperate based on name
    name = models.CharField(max_length=150)

    class Type(models.TextChoices):
        Gaussian = 'Gaussian', _('Gaussian')
        Primitive = 'Primitive', _('Primitive')
        CORPSE = 'CORPSE', _('CORPSE')
        CinBB = 'CinBB', _('CinBB')
        CinSK = 'CinSK', _('CinSK')
    # can be extended when required, is valid based on type
    type = models.CharField(
        max_length=10,
        choices=Type.choices,
        default=Type.CinBB,
    )
    
    #with rabi rate validate to make sure it is between 0 and 100
    maximum_rabi_rate = models.DecimalField(
        default=1.0,
        max_digits=9, 
        decimal_places=6,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
        )
        
    #Polar Angle with value validation but no unit check (checking if unit is in pi) 
    polar_angle = models.DecimalField(
        default=0.0,
        max_digits=9, 
        decimal_places=8,
        validators=[MaxValueValidator(1), MinValueValidator(0)]
        )


def __str__(self):
    return "{} - {} - {} - {}".format(self.name, self.type, self.maximum_rabi_rate, self.polar_angle)