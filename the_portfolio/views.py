from django.shortcuts import render , redirect
# Create your views here.


def index(request):
	objects = Object.objects.all()
	context = {'objects' : objects}
	return render(request, "the_portfolio/index.html" , context)