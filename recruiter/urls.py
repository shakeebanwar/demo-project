from django.urls import path,include
from .views import *

urlpatterns = [

#web urls  home

path('registration',registration.as_view(),name="registration"),

]