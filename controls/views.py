# views.py contains the logic behind search functionality, import and export functions and other test functions
# which were explored to gain a better grasp of api functionality

from django.shortcuts import render, get_object_or_404, HttpResponse
from tablib import Dataset
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter


from .resources import ControlResource
from .models import Controls
from .serializers import ControlSerializer

# View set to view entire control library with CRUD Capabilities
class BaseViewSet (ModelViewSet):
    __basic_fields = ('name', 'ctype', 'polar_angle')
    queryset = Controls.objects.all()
    serializer_class = ControlSerializer
    filer_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    order_fields = __basic_fields
    search_fields = __basic_fields
       

#Export View to export data in CSV, allowance for other data type for future use
def export_controls(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        control_resource = ControlResource()
        dataset = control_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
        return response
    return render(request, 'export.html')

#Import View to import data in CSV and JSON, allowance for other data type for future use
def import_controls(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        control_resource = ControlResource()
        dataset = Dataset()
        new_controls = request.FILES['importData']
        #Allowed to import data as CSV or JSON 
        if file_format == 'CSV':
            #required to load the data on
            imported_data = dataset.load(new_controls.read().decode('utf-8'),format='csv')
            result = control_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_controls.read().decode('utf-8'),format='json')
            # Testing data import
            result = control_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            control_resource.import_data(dataset, dry_run=False)

    return render(request, 'import.html')