from django.urls import path,include
from .views import *

urlpatterns = [

#web urls  home

path('login',login.as_view(),name="login"),
path('logout',logout.as_view()),
path('changepassword',changepassword.as_view()),
path('profile',profile.as_view()),
path('accountActivation',accountActivation.as_view()),
path('alljobs',alljobs.as_view()),




]