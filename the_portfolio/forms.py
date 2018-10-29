from django import forms 
from .models import *




class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title' , 'description' , 'repo_url']
        widgets = {
            'project_description' : forms.Textarea(attrs={'rows' : '3'})
        }