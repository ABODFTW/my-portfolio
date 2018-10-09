from django.shortcuts import render , redirect
from django.views import View
from django.views.generic.base import *
from django.views.generic.edit import * 
from .models import * 
from .forms import *


class index(TemplateView):
    template_name = 'the_portfolio/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context


class AddProject(CreateView):
    template_name = 'the_portfolio/add_project.html'
    form_class = AddProjectForm
    model = Project
    success_url = '/'