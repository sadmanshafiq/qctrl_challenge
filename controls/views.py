from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_json_api.parsers import JSONParser

from .models import Controls, Control_Types
from .serializers import ControlSerializer

# Basic view set to view entire control library
class BaseViewSet (ModelViewSet):
    __basic_fields = ('name', 'ctype', 'polar_angle')
    queryset = Controls.objects.all()
    serializer_class = ControlSerializer
    filer_backends = (filters.DjangoFilterBackend, SearchFilter,OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_control(request, pk):
    control = get_object_or_404(Controls, pk=pk)
    # get details of a single control
    if request.method == 'GET':
        serializer = ControlSerializer(control) 
        return Response(serializer.data)
    # delete a single control
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single control
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_control(request):
    # get all controls
    if request.method == 'GET':
        controls = Controls.objects.all()
        serializer = ControlSerializer(controls, many=True)
        return Response(serializer.data)
    # insert a new record for a control
    if request.method == 'POST':
        #data = {
        #    'name': request.data.get('name'),
        #    'ctype': Control_Types.objects.get(request.data.get('ctype')),
        #    'maximum_rabi_rate': request.data.get('maximum_rabi_rate'),
        #    'polar_angle': request.data.get('polar_angle')
        #}
        data = JSONParser().parse(request)

        serializer = ControlSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
