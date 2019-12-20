from django.shortcuts import render
from rest_framework import viewsets

from .models import Controls
from .serializers import ControlSerializer

class BaseViewSet (viewsets.ModelViewSet):
    queryset = Controls.objects.all()
    serializer_class = ControlSerializer

# Basic view set to view entire control library
