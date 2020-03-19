from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from Login.views import CustomAuthToken

from Login import views

urlpatterns = [
    re_path(r'login/$', CustomAuthToken.as_view()),
    re_path(r'example_list2/$',views.ExampleList2.as_view()),
    #Hola soy AlucardHJ123
]