# Map views to a URL to be able to access it in a browser
from django.urls import path

from . import views

# Define the paths within the polls and the location of the view and their method
urlpatterns = [
    path("", views.index, name="index"),
]