from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

'''
when the user requests it will go the controller check if req need 
data realted go to to model for Data manipulation
then model give the data back to the controller 
and then render to the views

~ MVC 


'''

# Create your views here.
def project_list(request):
   return render(request, 'projects/index.html')

def all_projects(request):
   # here to return a list of all projects by the db
   project = Project.objects.all()
   return render(request, 'projects/allprojects.html',   {'projects': project})

def projects_details(request, pk):
   # query the data from the db
   project = Project.objects.get(pk=pk)
   return render(request, 'projects/details.html', {'project':project})
