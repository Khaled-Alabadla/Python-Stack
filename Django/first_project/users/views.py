from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.

def index_root(request):
    return redirect('/blogs')

def register(request):
    return HttpResponse('placeholder for users to create a new user record.')

def login(request):
    return HttpResponse('placeholder for users to log in.')

def index(request):
    return HttpResponse('placeholder to display all the list of users later.')
