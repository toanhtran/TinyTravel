from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello Tiny Travelers!</h1>')
def index(request):
    return HttpResponse('This is the index page')
