#  where give the url of the project from django.contrib import admin
from django.urls import path ,include
from projects import views

app_name = 'projects'
# routes for the users requests 
# #  Linking: app_name,w
urlpatterns = [
    path('', views.all_projects,name='all_projects'),    
    path('',views.project_list),
    path("<int:pk>", views.projects_details,name='projects_details'),
]
