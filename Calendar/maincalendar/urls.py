from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", indexView.as_view(), name= "index-page"),
    path("process/", processView.as_view(), name="process-page"),
    path("test/", testView.as_view(), name="test-page"),
]

