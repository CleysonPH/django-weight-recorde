from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("weight_recorder.urls", namespace="weight_recorder")),
    path('admin/', admin.site.urls),
]
