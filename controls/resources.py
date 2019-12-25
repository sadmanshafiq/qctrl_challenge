#resources.py is used by import_export to insert controls and export controls in the method specified csv format

from import_export import resources
from .models import Controls

# Register your Resources here.
class ControlResource(resources.ModelResource):
    class Meta:
        model = Controls
        exclude = ('id', )