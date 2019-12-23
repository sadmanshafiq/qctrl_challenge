from rest_framework_json_api import serializers
from .models import Controls
#class ControlTypeSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Control_Types
#        fields = ("control_types")

class ControlSerializer(serializers.ModelSerializer): 
#    ctype = ControlTypeSerializer()
    class Meta:
        model = Controls
        fields = ("name","ctype","maximum_rabi_rate","polar_angle")
