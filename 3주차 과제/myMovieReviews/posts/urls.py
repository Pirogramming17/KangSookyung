from django.urls import path, include 
from django.contrib import admin

from . import views

app_name = "posts"


urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('review/<int:id>', views.detail, name="detail"),
    path('modify/<int:id>', views.modify, name="modify"),
    path('delete/<int:id>', views.delete, name="delete"),
]