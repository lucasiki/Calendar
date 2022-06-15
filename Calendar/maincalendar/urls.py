from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", indexView.as_view(), name= "index-page"),
    path("process/", processView.as_view(), name="process-page"),
    path("widget/", widgetView.as_view(), name="widget-page"),
    path("hour-widget/", hourWidgetView.as_view(), name="hour-widget-page"),
    path("test/", testView.as_view(), name="test-page"),
]

