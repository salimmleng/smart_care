from django.contrib import admin
from .models import Patient
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'image','mobile_no']

    # relationship e thakle evabe first name and last name ke access korte hobe
    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name

admin.site.register(Patient,PatientAdmin)
