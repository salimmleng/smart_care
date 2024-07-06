from django.shortcuts import render
from rest_framework import viewsets,pagination
from .import serializers
from .import models 
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters



# handle pagination

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100


class DoctorViewSet(viewsets.ModelViewSet):

    queryset = models.Doctor.objects.all() # data asbe
    serializer_class = serializers.DoctorSerializer # data json formate e convert hobe
    pagination_class = DoctorPagination




class SpecializationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = models.Specialization.objects.all() # data asbe
    serializer_class = serializers.SpecializationSerializer # data json formate e convert hobe


class DesignationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Designation.objects.all() # data asbe
    serializer_class = serializers.DesignationSerializer # data json formate e convert hobe


class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):

    def filter_queryset(self,request,query_set,view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set




class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.AvailableTime.objects.all() # data asbe
    serializer_class = serializers.AvailableTimeSerializer # data json formate e convert hobe
    filter_backends = [AvailableTimeForSpecificDoctor]


class ReviewViewSet(viewsets.ModelViewSet):

    queryset = models.Review.objects.all() # data asbe
    serializer_class = serializers.ReviewSerializer # d

