from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Controls, Control_Types
from .serializers import ControlSerializer

# Basic view set to view entire control library
class BaseViewSet (ModelViewSet):
    queryset = Controls.objects.all()
    serializer_class = ControlSerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_control(request, pk):
    try:
        control = Controls.objects.get(pk=pk)
    except Controls.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

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
    elif request.method == 'POST':
        return Response({})
