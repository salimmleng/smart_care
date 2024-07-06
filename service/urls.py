from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter() # ameder router
router.register('', views.ServiceViewSet) # router er antena

urlpatterns = [
    path('', include(router.urls)),
]

