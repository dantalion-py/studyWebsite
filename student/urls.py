from rest_framework import routers
from django.urls import path
from student import views


urlpatterns = [
    path('', views.home, name="hello")


]
