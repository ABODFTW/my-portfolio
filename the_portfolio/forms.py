from django import forms 
from .models import *




class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name' , 'project_description']
        widgets = {
            'project_description' : forms.Textarea(attrs={'rows' : '3'})
        }