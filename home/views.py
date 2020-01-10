from django.shortcuts import render

from auction.models import Lot

def index(request):
    """ Return render index page """

    featured_lots = Lot.objects.filter(featured=True)[0:6]
    military = Lot.objects.filter(category='military')[0:6]
    cultural = Lot.objects.filter(category='cultural')[0:6]
    weapons = Lot.objects.filter(category='weapons')[0:6]
    real_estate = Lot.objects.filter(category='real estate')[0:6]

    context = {
        'featured_lots': featured_lots,
        'military': military,
        'cultural': cultural,
        'weapons': weapons,
        'real_estate': real_estate

    }

    return render(request, 'index.html', context)
