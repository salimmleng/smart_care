from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter() # ameder router
router.register('doctor_list', views.DoctorViewSet) # router er antena
router.register('designation', views.DesignationViewSet) # router er antena
router.register('specialization', views.SpecializationViewSet) # router er antena
router.register('available_time', views.AvailableTimeViewSet) # router er antena
router.register('reviews', views.ReviewViewSet) # router er antena

urlpatterns = [
    path('', include(router.urls)),
]

