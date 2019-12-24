from import_export import resources
from .models import Controls

# Register your Resources here.
class ControlResource(resources.ModelResource):
    class Meta:
        model = Controls
        exclude = ('id', )