from datetime import datetime

from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

from auction.models import Auction, Lot, Bid
from home.views import index
from .forms import BidForm

@login_required
def all_lot_items(request):
    """ Return all lot items in the DB """

    lot_objects = Lot.objects.all()
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


@login_required
def lot(request, lot_id):
    """ Return a detailed view of a lot item """

    lot = get_object_or_404(Lot, pk=lot_id)
    
    return render(request, 'lot.html', {'lot': lot})


@login_required
def all_auctions(request):
    """ Render all auctions """

    all_auctions = Auction.objects.all()

    return render(request, 'auctions.html', {'all_auctions': all_auctions})


@login_required
def auction(request, auction_id):
    """ Render the auction """

    auction = get_object_or_404(Auction, id=auction_id)
    bid = Bid.objects.filter(auction=auction_id).order_by('-bid_time')
    latest_bid = bid[0]
    buy_now = auction.buy_now
    bid_form = BidForm()

    context = {
        'auction': auction,
        'latest_bid': latest_bid,
        'buy_now': buy_now,
        'bid_form': bid_form
    }

    return render(request, 'auction.html', context)


@login_required
def bid(request, auction_id):
    """ Bid on auction. Bid must be higher than current bid """

    auction = get_object_or_404(Auction, id=auction_id)
    bid = get_object_or_404(Bid, id=auction_id)
    current_bid = bid.bid_amount
    current_user = auth.get_user(request)

    if request.method == 'POST':
        bid_form = BidForm(request.POST)

    if bid_form.is_valid():
        bid = Bid()
        if current_bid < bid_form.cleaned_data['bid_amount']:
            bid.user = current_user
            bid.auction = auction
            bid.bid_time = datetime.now()
            bid.bid_amount = bid_form.cleaned_data['bid_amount']
            bid.save()
            messages.success(request, 'Bid successfull. Good Luck!')
        else:
            messages.success(request, 'Bid must be higher than current bid')
            return redirect('auction', auction_id=auction_id)
    else:
        bid_form = BidForm()

    return redirect('auction', auction_id=auction_id)


