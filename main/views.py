from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#
# def home(request):
#     return HttpResponse('<h1>Hello Tiny Travelers!</h1>')
def home(request):
    context = {'locations':locations }
    return render(request, 'index.html', context)

class Location:
    def __init__(self, city, state, img_url):
        self.city = city
        self.state = state
        self.img_url = img_url

locations = [
    Location("Fool's Falls", "CO",
             'http://courseware.codeschool.com/try_django/images/fools-falls.jpg'),
    Location("Curly's Creek", "NM",
             'http://courseware.codeschool.com/try_django/images/curlys-creek.jpg'),
    Location("The Delicate Arch", "UT", 'http://courseware.codeschool.com/try_django/images/delicate-arch.jpg')
]
