from django.shortcuts import render , redirect
from .models import Object
# Create your views here.


def index(request):
	objects = Object.objects.all()
	context = {'objects' : objects}
	return render(request, "the_portfolio/index.html" , context)
def crazy(request):
	if request.method == "POST":
		object_name = request.POST.get('object_name')
		Object.objects.create(object_name=object_name)
		return redirect('index')

	return render(request , 'the_portfolio/create_object.html')