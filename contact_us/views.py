from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .serializers import ContactUsSerializer
from .models import ContactUs 
class ContactUsViewSet(viewsets.ModelViewSet):

    queryset = ContactUs.objects.all() # data asbe
    serializer_class = ContactUsSerializer # data json formate e convert hobe


