from django.utils import timezone

from celery import shared_task 
from celery.utils.log import get_task_logger

from auction.models import Auction, Bid


logger = get_task_logger(__name__)


@shared_task(name='auction.tasks.task_set_auction_to_expire') 
def task_set_auction_to_expire():
    """
    Set auction.expire to True if the auction is over
    """
    auctions = Auction.objects.all()

    for auction in auctions:
        if auction.expired != True: 
            if auction.time_ending < timezone.now():
                auction.expired = True
                bid = Bid.objects.filter(auction=auction.pk).order_by('-bid_time')
                if bid:                                 
                    latest_bid = bid[0]
                    auction.winner = latest_bid.user
                    auction.save()
                    logger.info("Expired and winner set.")
                else:
                    logger.info("Bid not found")
            else:
                logger.info("Auction not expired, aborted function")
                return
        else:
            logger.info("Auction expired")
            return

    