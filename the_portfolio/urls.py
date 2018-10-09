from django.urls import path , include

from . import views

urlpatterns = [
    path('' , views.index.as_view() , name="index" ),
    path('add-project' , views.AddProject.as_view() , name='add-project')
]
