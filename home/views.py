from django.shortcuts import render

from auction.models import Lot

def index(request):
    """ Return render index page """

    featured_lots = Lot.objects.filter(featured=True)

    return render(request, 'index.html', {'featured_lots': featured_lots})
