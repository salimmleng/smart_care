from django.shortcuts import render
from .import serializers
from .import models
from rest_framework import viewsets

# Create your views here.

class AppointmentViewSets(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppoinmentSerializer
    
    # ekta patient er koyta appointment ase patient_id=1 or patient_id=2
    def get_queryset(self):
        queryset = super().get_queryset() # 9 no line ke niye aslam ba parent ke inherit korlamn
        print(self.request.query_params)
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id = patient_id) # patient id thakle eta excetue hobe na hole 9 no line excute hobe 

        return queryset
    


    # ekta doctor er koyta appointment ase doctor_id=2 or doctor_id=1
    def get_queryset(self):
        queryset = super().get_queryset()
        doctor_id = self.request.query_params.get("doctor_id")
        if doctor_id:
            queryset = queryset.filter(doctor_id = doctor_id)

        return queryset


        


