import csv, io
from django.shortcuts import render #, get_object_or_404, HttpResponse
from tablib import Dataset
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
#removed as not used in final instance
#from rest_framework.decorators import api_view, parser_classes

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
        #Allowed to export d
        if file_format == 'CSV':
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

#def testpage(request):
#    my_dict = {"insert_me": "I am from views.py"}
#    return render(request,'test.html',context=my_dict)

#def control_download(request):
#    control = Controls.objects.all()

#    response = HttpResponse(content_type='text/csv')
#    response['Content-Disposition'] = 'attachment; filename="controls.csv"'

#    writer = csv.writer(response, delimiter=',')
#    writer.writerow(['name', 'type', 'maximum_rabi_rate', 'polar_angle'])

#    for obj in control:
#        writer.writerow([obj.name, obj.ctype, obj.maximum_rabi_rate, obj.polar_angle])
#    return response

#@api_view(['GET', 'DELETE', 'PUT'])
#def get_delete_update_control(request, pk):
#    control = get_object_or_404(Controls, pk=pk)
    # get details of a single control
#    if request.method == 'GET':
#        serializer = ControlSerializer(control) 
#        return Response(serializer.data)
    # delete a single control
#    if request.method == 'DELETE':
#        control.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single control
#    if request.method == 'PUT':
#        serializer = ControlSerializer(control, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#@api_view(['GET', 'POST'])
#def get_post_control(request):
    # get all controls
#    if request.method == 'GET':
#        controls = Controls.objects.all()
#        serializer = ControlSerializer(controls, many=True)
#        return Response(serializer.data)
    # insert a new record for a control
#    if request.method == 'POST':
#        data = {
#            'name': request.data.get('name'),
#            'ctype': request.data.get('ctype'),
#            'maximum_rabi_rate': request.data.get('maximum_rabi_rate'),
#            'polar_angle': request.data.get('polar_angle')
#        }

#        serializer = ControlSerializer(data=data ) #many=isinstance(request.data, list
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
