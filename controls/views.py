import csv, io
from django.shortcuts import render, get_object_or_404, HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, parser_classes, action
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework_csv.parsers import CSVParser
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Controls
from .serializers import ControlSerializer

# Proper view set to view entire control library
class BaseViewSet (ModelViewSet):
    __basic_fields = ('name', 'ctype', 'polar_angle')
    queryset = Controls.objects.all()
    serializer_class = ControlSerializer
    filer_backends = (filters.DjangoFilterBackend, SearchFilter)
    search_fields = __basic_fields

class UploadView(ModelViewSet):
    queryset = Controls.objects.all()
    serializer_class = ControlSerializer
    parser_classes = (JSONParser, MultiPartParser, CSVParser)

    @action(detail=False, methods=['put'], name='upload', parser_classes=[CSVParser],)
    def upload(self, request, filename, format=None):
        data = request.data
        return Response(status=status.HTTP_204_NO_CONTENT)

def control_download(request):
    control = Controls.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="controls.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['name', 'type', 'maximum_rabi_rate', 'polar_angle'])

    for obj in control:
        writer.writerow([obj.name, obj.ctype, obj.maximum_rabi_rate, obj.polar_angle])
    return response

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_control(request, pk):
    control = get_object_or_404(Controls, pk=pk)
    # get details of a single control
    if request.method == 'GET':
        serializer = ControlSerializer(control) 
        return Response(serializer.data)
    # delete a single control
    if request.method == 'DELETE':
        control.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single control
    if request.method == 'PUT':
        serializer = ControlSerializer(control, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_control(request):
    # get all controls
    if request.method == 'GET':
        controls = Controls.objects.all()
        serializer = ControlSerializer(controls, many=True)
        return Response(serializer.data)
    # insert a new record for a control
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'ctype': request.data.get('ctype'),
            'maximum_rabi_rate': request.data.get('maximum_rabi_rate'),
            'polar_angle': request.data.get('polar_angle')
        }

        serializer = ControlSerializer(data=data ) #many=isinstance(request.data, list
        if serializer.is_valid():
            serializer.save()
            #if isinstance(serializer.validated_data, list):
            #    response_status = some_function_to_create_objects_in_batch(serializer.validated_data)
            #    return Response(data, response_status)
            #else:
            #    response_status = some_function_to_create_objects_in_batch(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
