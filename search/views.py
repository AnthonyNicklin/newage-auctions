from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from auction.models import Lot


def keyword_search(request):
    """ Use keyword submitted to return list of current auctions """

    if request.method == 'GET':
        keyword = request.GET.get('q')

        keyword_obj = []

        if keyword is None or keyword == "":
            messages.error(request, 'Please enter in a keyword to search')
            return redirect('all_auctions')

        elif keyword:
            keyword_lookup = Lot.objects.filter(Q(name__icontains=keyword) | \
                Q(description__icontains=keyword))
            for item in keyword_lookup:
                keyword_obj.append(item)
            
            paginator = Paginator(keyword_obj, 10)

            page = request.GET.get('page')

            try:
                current_items = paginator.page(page)
            except PageNotAnInteger:
                # If the page is not an integer, deliver first page.
                current_items = paginator.page(1)
            except EmptyPage:
                # If page is not an integer, deliver first page.
                current_items = paginator.page(paginator.num_pages)

            return render(request, 'search.html', {'current_items': current_items})
    else:
        return redirect('all_auctions')


