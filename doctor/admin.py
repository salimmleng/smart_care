from django.contrib import admin
from .models import Doctor,Designation,Specialization,AvailableTime,Review
# Register your models here.

admin.site.register(Doctor)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",),}

admin.site.register(Designation,DesignationAdmin)

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",),}


admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(AvailableTime)
admin.site.register(Review)

