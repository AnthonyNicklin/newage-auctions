from django.shortcuts import render

from auction.models import Lot


def index(request):
    """ Return index page with feature lots """

    featured_lots = Lot.objects.filter(featured=True)[0:6]

    return render(request, 'index.html', {'featured_lots': featured_lots})


def not_found(request):
    """ Return 404 page not found """

    return render(request, '404.html')


def server_error(request):
    """ Return 500 internal server error """

    return render(request, '500.html')