from django.urls import path

from . import views


app_name = "weight_recorder"
urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("peso/adicionar", views.weight_create, name="weight_create"),
    path("peso/<int:pk>/editar", views.weight_edit, name="weight_edit"),
    path("peso/<int:pk>/apagar", views.weight_delete, name="weight_delete"),
]
