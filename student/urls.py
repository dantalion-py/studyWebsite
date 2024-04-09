from rest_framework import routers
from django.urls import path
from student import views


urlpatterns = [
    path('hello/', views.home, name="hello")


]
