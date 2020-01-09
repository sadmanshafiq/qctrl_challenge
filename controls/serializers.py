# serializers.py contains the serializers for controls and controltypes
# controltype was depreciated due to model matching errors.

from rest_framework_json_api import serializers
from .models import Controls

class ControlSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Controls
        fields = ("name","type","maximum_rabi_rate","polar_angle")
    
