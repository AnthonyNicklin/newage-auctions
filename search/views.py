from datetime import datetime

from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from auction.models import Lot, Auction


def keyword_search_lots(request):
    """ Use keyword submitted to return list of current lots """

    if request.method == 'GET':
        keyword = request.GET.get('q')

        keyword_obj = []

        if keyword is None or keyword == "":
            messages.error(request, 'Please enter in a keyword to search')
            return redirect('all_lot_items')

        elif keyword:
            keyword_lookup = Lot.objects.filter(Q(name__icontains=keyword) | \
                Q(description__icontains=keyword))
            for item in keyword_lookup:
                keyword_obj.append(item)
            
            paginator = Paginator(keyword_obj, 10)

            page = request.GET.get('page')

            try:
                lot_items = paginator.page(page)
            except PageNotAnInteger:
                # If the page is not an integer, deliver first page.
                lot_items = paginator.page(1)
            except EmptyPage:
                # If page is not an integer, deliver first page.
                lot_items = paginator.page(paginator.num_pages)

            return render(request, 'lot_items.html', {'lot_items': lot_items})
    else:
        return redirect('all_lot_items')


def keyword_search_auctions(request):
    """ Use keyword submitted to return list of auctions """

    if request.method == 'GET':
        keyword = request.GET.get('q')

        keyword_obj = []

        if keyword is None or keyword == "":
            messages.error(request, 'Please enter in a keyword to search')
            return redirect('all_auctions')

        elif keyword:
            keyword_lookup = Auction.objects.filter(Q(description__icontains=keyword))
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

            return render(request, 'auctions.html', {'current_items': current_items})
    else:
        return redirect('all_auctions')


def category(request, category):
    """ Render lots based on category the user has clicked on """

    today = datetime.today()
    lot_objects = Lot.objects.filter(category=category)
    
    try:
        lot_objects = Lot.objects.filter(category=category).exclude(auction__time_ending__lt=today)
    except:
        messages.info(request, 'Sorry there are no Lots in this category at this time')
        return redirect('lots')

    paginator = Paginator(lot_objects, 10)

    page = request.GET.get('page')
    try:
        lot_items = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver first page.
        lot_items = paginator.page(1)
    except EmptyPage:
        # If page is not an integer, deliver first page.
        lot_items = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'lot_items': lot_items, 'category': category})


