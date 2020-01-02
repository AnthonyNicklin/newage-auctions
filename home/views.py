from django.shortcuts import render

from auction.models import Lot

def index(request):
    """ Return render index page """

    featured_lots = Lot.objects.filter(featured=True)
    military = Lot.objects.filter(category='military')
    cultural = Lot.objects.filter(category='cultural')
    weapons = Lot.objects.filter(category='weapons')
    real_estate = Lot.objects.filter(category='real estate')

    context = {
        'featured_lots': featured_lots,
        'military': military,
        'cultural': cultural,
        'weapons': weapons,
        'real_estate': real_estate

    }

    return render(request, 'index.html', context)
