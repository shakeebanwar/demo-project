from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'registration', Registration, basename='registration')

urlpatterns = [
    path('', include(router.urls)),
]