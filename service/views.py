from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .serializers import ServiceSerializer
from .models import Service 
class ServiceViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all() # data asbe
    serializer_class = ServiceSerializer # data json formate e convert hobe

