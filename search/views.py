from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages

from auction.models import Lot


def keyword_search(request):
    """ Use keyword submitted to return list of current auctions """

    if request.method == 'GET':
        keyword = request.GET.get('q')

        current_items = []

        if keyword is None or keyword == "":
            messages.error(request, 'Please enter in a keyword to search')
            return redirect('all_auctions')

        elif keyword:
            keyword_lookup = Lot.objects.filter(Q(name__icontains=keyword) | \
                Q(description__icontains=keyword))
            for item in keyword_lookup:
                current_items.append(item)
        
            return render(request, 'search.html', {'current_items': current_items})
    else:
        return redirect('all_auctions')


