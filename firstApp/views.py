from django.shortcuts import render
from django.http import HttpResponse
from .models import Person  # added

# Create your views here.


def index(request):
    persons = Person.objects.all()  # added
    data_dict = dict()  # added
    data_dict['persons'] = persons  # added
    return render(request, 'firstApp/index.html', data_dict)


def about(request):
    return render(request, 'firstApp/about.html')


def form(request):
    return render(request, 'firstApp/form.html')

# added


def greet(request):
    first_name = request.POST.get('fName')  # added
    last_name = request.POST.get('lName')  # added
    name = first_name + ' ' + last_name  # added
    return render(request, 'firstApp/greet.html', {'name': name})  # added
