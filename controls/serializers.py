from rest_framework_json_api import serializers
from .models import Controls

class ControlSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Controls
        fields = ("name","ctype","maximum_rabi_rate","polar_angle")