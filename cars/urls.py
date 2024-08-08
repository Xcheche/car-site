from django.urls import path
from . import views


app_name = "cars"
urlpatterns = [
    path("", views.carlist, name="carlist"),
    path("add/", views.add, name="add"),
    path("delete/", views.delete, name="delete"),
    path("update/<int:pk>/", views.update, name="update"),
]