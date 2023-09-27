from django.urls import path
from . import views


app_name = 'myblog'
urlpatterns = [
    path('', views.myblog, name='myblog'),
    # Other URL patterns go here
    path('post', views.post, name='myblog'),
]