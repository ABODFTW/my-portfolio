from django.shortcuts import render , redirect
from django.views import View
from django.views.generic.base import *
from django.views.generic.edit import * 
from .models import * 
# Create your views here.

class index(TemplateView):
	template_name = 'the_portfolio/index.html'

class AddProject(CreateView):
	template_name = 'the_portfolio/add_project.html'
	model = Project
	fields = ['project_name' , 'project_description']
	success_url = '/'