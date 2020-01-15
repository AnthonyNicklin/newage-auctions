from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime

from auction.models import Lot, Auction, Bid


class LotModelTest(TestCase):
    """ Tests fot the Lot model """
    @classmethod
    # Set up non-modified objects used by all test methods
    def setUpTestData(cls):
        Lot.objects.create(id=1, name='Tommy Gun', origin='USA', 
            description="Gun used by gangsters in the 50's", age=50, category='military')

    def test_name_label(self):
        lot_obj = Lot.objects.get(id=1)
        field_label = lot_obj._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        lot_obj = Lot.objects.get(id=1)
        max_length = lot_obj._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_origin_label(self):
        lot_obj = Lot.objects.get(id=1)
        field_label = lot_obj._meta.get_field('origin').verbose_name
        self.assertEquals(field_label, 'origin')

    def test_origin_max_length(self):
        lot_obj = Lot.objects.get(id=1)
        max_length = lot_obj._meta.get_field('origin').max_length
        self.assertEquals(max_length, 200)

    def test_description_label(self):
        lot_obj = Lot.objects.get(id=1)
        field_label = lot_obj._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')
    
    def test_age_label(self):
        lot_obj = Lot.objects.get(id=1)
        field_label = lot_obj._meta.get_field('age').verbose_name
        self.assertEquals(field_label, 'age')

    
class AuctionModelTest(TestCase):
    """ Tests for the Auction model """
    @classmethod
    # Set up non-modified objects used by all test methods
    def setUpTestData(cls):
        Lot.objects.create(id=1, name='Tommy Gun', origin='USA', 
            description="Gun used by gangsters in the 50's", age=50, category='military')
        user = User.objects.create_user(
            username='John12', email='john.smith@gmail.com', password='akdf34983!',
            first_name='John', last_name='Smith'
        )
        user.save()
        lot_obj = Lot.objects.get(id=1)
        user_obj = User.objects.get(id=1)
        Auction.objects.create(id=1, lot=lot_obj, description='Testing model',
            number_of_bids=3, time_starting=datetime.now(),
            time_ending="2020-02-02 16:30", expired=False,
            winner=user_obj, winning_bid=40.00, paid=False)

    def test_lot_label(self):
        auction_obj = Auction.objects.get(id=1)
        field_label = auction_obj._meta.get_field('lot').verbose_name
        self.assertEquals(field_label, 'lot')
    
    def test_description_label(self):
        auction_obj = Auction.objects.get(id=1)
        field_label = auction_obj._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_number_of_bids_label(self):
        auction_obj = Auction.objects.get(id=1)
        field_label = auction_obj._meta.get_field('number_of_bids').verbose_name
        self.assertEquals(field_label, 'number of bids')

    def test_time_starting_label(self):
        auction_obj = Auction.objects.get(id=1)
        field_label = auction_obj._meta.get_field('time_starting').verbose_name
        self.assertEquals(field_label, 'time starting')

    def test_time_ending_label(self):
        auction_obj = Auction.objects.get(id=1)
        field_label = auction_obj._meta.get_field('time_ending').verbose_name
        self.assertEquals(field_label, 'time ending')

    def test_expired_label(self):
        auction_obj = Auction.objects.get(id=1)
        field_label = auction_obj._meta.get_field('expired').verbose_name
        self.assertEquals(field_label, 'expired')
        
    def test_winner_label(self):
        auction_obj = Auction.objects.get(id=1)
        field_label = auction_obj._meta.get_field('winner').verbose_name
        self.assertEquals(field_label, 'winner')

    def test_winning_bid_label(self):
        auction_obj = Auction.objects.get(id=1)
        field_label = auction_obj._meta.get_field('winning_bid').verbose_name
        self.assertEquals(field_label, 'winning bid')

    def test_paid_label(self):
        auction_obj = Auction.objects.get(id=1)
        field_label = auction_obj._meta.get_field('paid').verbose_name
        self.assertEquals(field_label, 'paid')
        

class BidModelTest(TestCase):
    """ Tests for the Bid model """
    @classmethod
    # Set up non-modified objects used by all test methods
    def setUpTestData(cls):
        Lot.objects.create(id=1, name='Tommy Gun', origin='USA', 
            description="Gun used by gangsters in the 50's", age=50, category='military')
        user = User.objects.create_user(
            username='John12', email='john.smith@gmail.com', password='akdf34983!',
            first_name='John', last_name='Smith'
        )
        user.save()
        lot_obj = Lot.objects.get(id=1)
        user_obj = User.objects.get(id=1)
        Auction.objects.create(id=1, lot=lot_obj, description='Testing model',
            number_of_bids=3, time_starting=datetime.now(),
            time_ending="2020-02-02 16:30", expired=False,
            winner=user_obj, winning_bid=40.00, paid=False)
        auction_obj = Auction.objects.get(id=1)
        Bid.objects.create(id=1, auction=auction_obj, user=user_obj, bid_amount=9999999.99,
            bid_time=datetime.now())

    def test_bid_amount_label(self):
        bid_obj = Bid.objects.get(id=1)
        field_label = bid_obj._meta.get_field('bid_amount').verbose_name
        self.assertEquals(field_label, 'bid amount')

    def test_bid_time_label(self):
        bid_obj = Bid.objects.get(id=1)
        field_label = bid_obj._meta.get_field('bid_time').verbose_name
        self.assertEquals(field_label, 'bid time')