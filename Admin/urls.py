from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'authentication', Authentication, basename='authentication')
router.register(r'profile', AdminProfile, basename='profile')
router.register(r'accountactivation', AccountActivation, basename='accountactivation')

urlpatterns = [
    path('', include(router.urls)),
]