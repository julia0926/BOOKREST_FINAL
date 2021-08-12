from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.category, name="category"),
    #path('search', views.search, name="search"),
    path("detail/<str:id>", views.detail, name="detail"),
    path("detail/borrows/<str:id>", views.borrow, name="borrow"),
    path("detail/whishes/<str:id>", views.wish, name="wish"),
]