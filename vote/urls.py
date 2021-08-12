from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.vote, name="vote"),
]