# here where give the url of the project from django.contrib import admin
from django.urls import path ,include
from projects import views

urlpatterns = [
    path('',views.project_list)
]
