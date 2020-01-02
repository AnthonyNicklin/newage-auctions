from django.test import TestCase

from auction.forms import BidForm

class TestBidForm(TestCase):

    def test_can_create_bid(self):
        form = BidForm({'bid_amount': '100.00'})
        self.assertTrue(form.is_valid())


