from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project


def myblog(request):
    return render(request, 'myblogs/blog.html')

def post(request, *args, **kwargs):
    return render(request, 'posts/post.html')