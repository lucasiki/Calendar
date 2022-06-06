from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", indexView.as_view(), name= "index-page"),
    path("day/", dayView.as_view(), name= "day-page"),
]