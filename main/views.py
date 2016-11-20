from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#
# def home(request):
#     return HttpResponse('<h1>Hello Tiny Travelers!</h1>')
def home(request):
    name = "Phillip Kaggie"
    age = "0-12 months"
    context = {'tiny_traveler_name': name,
                'tiny_traveler_age': age }
    return render(request, 'index.html', context)
