from django.urls import path , include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('' , views.index.as_view() , name="index" ),
    path('add-project' , login_required(views.AddProject.as_view()) , name='add-project'),
]
