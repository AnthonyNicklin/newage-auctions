from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone

from celery import shared_task 
from celery.utils.log import get_task_logger

from auction.models import Auction, Bid
from cart.views import add_to_cart


logger = get_task_logger(__name__)


@shared_task(name='auction.tasks.task_set_auction_to_expire') 
def task_set_auction_to_expire():
    """
    Set auction.expire to True if the auction is over
    """
    auctions = Auction.objects.all()

    for auction in auctions:
        if auction.expired != True and auction.time_ending < timezone.now():
            auction.expired = True
            auction.save()
            logger.info("Expired set")
        else:
            logger.info("Auction not expired, aborted function")
            return


# @shared_task(name='auction.tasks.task_set_winner_of_auction')
# def task_set_winner_of_auction():
#     """ 
#     If auction.expire is True find the winning 
#     bid and bind to the user who won 
#     """
#     auctions = Auction.objects.all()
#     user = User.objects.get(pk=request.user.id)

#     for auction in auctions:
#         if auction.expired:
#             bid = Bid.objects.filter(auction=auction.pk).order_by('-bid_time')
#             if bid:                                 
#                 latest_bid = bid[0]
#                 if latest_bid.user_id == user.id:
#                     add_to_cart(request, auction.pk)
#                     logger.info("Winner found and added to cart")
#                 else:
#                     logger.info("No user found for winning bid")
#             else:
#                 logger.info("Bid not found")
#                 return
#         else:
#             logger.info("Auction not expired")
#             return