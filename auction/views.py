from django.utils import timezone
from datetime import datetime

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

from auction.models import Auction, Lot, Bid
from home.views import index
from .forms import BidForm


@login_required
def auction(request, auction_id):
    """ Render the auction """

    auction = get_object_or_404(Auction, auction_id=auction_id)
    bid_form = BidForm()

    context = {
        'bid_form': bid_form,
        'auction': auction,
    }

    return render(request, 'auction', context)


@login_required
def bid(request, auction_id):
    """ Function for user to bid on auction """

    auction = Auction.objects.filter(id=auction_id)
    if auction[0].time_starting > timezone.now():
        return index(request)

    user = auth.get_user(request)

    latest_bid = Bid.objects.all().order_by('-bid_time')
    if latest_bid:
        winning_bid = latest_bid[0].bid_amount
            
    context = {
        'user': user,
        'winning_bid': winning_bid
    }

    return render(request, 'auction', context)


