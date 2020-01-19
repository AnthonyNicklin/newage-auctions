from datetime import datetime

from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q

from auction.models import Auction, Lot, Bid
from home.views import index
from .forms import BidForm


def all_lot_items(request):
    """ Return all lot items in the DB """

    try:
        lot_objects = Lot.objects.all()
    except:
        messages.info(request, 'Sorry there are Lots in stock at this time')
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

    return render(request, 'lot_items.html', {'lot_items': lot_items})


def lot(request, lot_id):
    """ Return a detailed view of a lot item """

    lot = get_object_or_404(Lot, pk=lot_id)
    
    return render(request, 'lot.html', {'lot': lot})


def all_auctions(request):
    """ Render all auctions """

    today = datetime.today()
    auctions_obj = Auction.objects.filter(time_ending__gte=today)
    paginator = Paginator(auctions_obj, 10)

    page = request.GET.get('page')

    try:
        current_items = paginator.page(page)
    except PageNotAnInteger:
        current_items = paginator.page(1)
    except EmptyPage:
        current_items = paginator.page(paginator.num_pages)

    return render(request, 'auctions.html', {'current_items': current_items})


def auction(request, auction_id):
    """ Render the auction """

    auction = get_object_or_404(Auction, id=auction_id)
    bid = Bid.objects.filter(auction=auction_id).order_by('-bid_time')
    bid_form = BidForm()

    if auction:
        if auction.time_ending > timezone.now():   
            if bid:                                 # If bid[0] False create first bid for auction
                latest_bid = bid[0]                 
            else:
                bid_default = Bid()
                bid_default.user = get_object_or_404(User, id=1)
                bid_default.auction = auction
                bid_default.bid_time = auction.time_starting
                bid_default.bid_amount = 0.00
                bid_default.save()
                latest_bid = bid_default

            if auction.time_starting < timezone.now():  # If the auction has not started yet
                context = {                             # hide the bid form.
                    'auction': auction,
                    'latest_bid': latest_bid,
                    'bid_form': bid_form
                }
            else: 
                context = {
                    'auction': auction,
                    'latest_bid': latest_bid
                }

            return render(request, 'auction.html', context)
        else:
            context = {
                'auction': auction,
            }

            return render(request, 'auction_expired.html', context)
    else:
        return render(request, '404.html')

@login_required
def lot_sold(request, auction_id):
    """ Render page stating the lot has expired and lot has been sold """

    auction = get_object_or_404(Auction, id=auction_id)

    if auction.paid:
        return render(request, 'lot_sold.html', {'auction': auction})
    else:
        return render(request, '404.html')


@login_required
def bid(request, auction_id):
    """ Bid on auction. Bid must be higher than current bid """

    auction = get_object_or_404(Auction, id=auction_id)
    bid = Bid.objects.filter(auction=auction_id).order_by('-bid_time')
    current_bid = bid[0].bid_amount
    current_user = auth.get_user(request)

    if request.method == 'POST':
        bid_form = BidForm(request.POST)

    if bid_form.is_valid():
        bid = Bid()
        if current_bid < bid_form.cleaned_data['bid_amount'] and \
            auction.time_starting < timezone.now():
            bid.user = current_user
            bid.auction = auction
            bid.bid_time = datetime.now()
            bid.bid_amount = bid_form.cleaned_data['bid_amount']
            bid.save()
            auction.number_of_bids += 1
            auction.save()
            messages.success(request, 'Bid successfull. Good Luck!')
        else:
            messages.error(request, 'Bid must be higher than current bid')
            return redirect('auction', auction_id=auction_id)
    else:
        bid_form = BidForm()

    return redirect('auction', auction_id=auction_id)


