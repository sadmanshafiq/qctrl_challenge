from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
#class Control_Types(models.Model):
#    control_types = models.CharField(max_length=30, blank=True)
#
#    def __unicode__(self):
#        return self.control_types

class Controls(models.Model):
    #Contains all the API parts, with choice explanation given

    #simple char field can be made unique if there was need to seperate based on name
    name = models.CharField(max_length=150)
    #with a control type you want to make sure you can swap out control types rather than destroy
    #ctype = models.ForeignKey(Control_Types, on_delete= models.PROTECT, blank=True, null=True)
    Gaussian = '1'
    
    class Type(models.TextChoices):
        Gaussian = 'GAUS', _('Gaussian')
        Primitive = 'PRIM', _('Primitive')
        CORPSE = 'CORP', _('CORPSE')
        CinBB = 'CINB', _('CinBB')
        CinSK = 'CINS', _('CinSK')
    # […]
    ctype = models.CharField(
        max_length=4,
        choices=Type.choices,
        default=Type.CinBB,
    )
    
    #with rabi rate validate to make sure it is 
    maximum_rabi_rate = models.DecimalField(
        default=1.0,
        max_digits=9, 
        decimal_places=6,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
        )
    #Polar Angle without unit validation (checking if unit in pi) 
    polar_angle = models.DecimalField(
        default=0.0,
        max_digits=9, 
        decimal_places=8,
        validators=[MaxValueValidator(1), MinValueValidator(0)]
        )


def __str__(self):
    return "{} - {}".format(self.name, self.ctype, self.maximum_rabi_rate, self.polar_angle)