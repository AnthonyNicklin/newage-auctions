from django.shortcuts import render

# Create your views here.

def index(request):
    """ Return render index page """

    return render(request, 'index.html')