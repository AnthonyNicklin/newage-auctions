from datetime import datetime

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.shortcuts import reverse

from auction.models import Lot, Auction

class LotViewTest(TestCase):
    @classmethod
    # Set up non-modified objects used by all test methods
    def setUpTestData(cls):
        lot = Lot.objects.create(id=1, name='Tommy Gun', origin='USA', 
            description="Gun used by gangsters in the 50's", age=50, category='military')
        lot.save()
        lot_two = Lot.objects.create(id=2, name='German Bayonet', origin='German', 
            description="Bayonet used in the battle of Berlin", age=75, category='weapons')
        lot_two.save()

        user = User.objects.create_user(username='Peter', email='pete.polo@gmail.com', password='addkj3245!')
        user.save()

        auction = Auction.objects.create(lot=lot, description='Greek Status of the God of War', 
            number_of_bids=5, time_starting='2020-01-01 16:10:10', time_ending='2030-01-15 16:10:10', 
            expired=False, winner=user, winning_bid=500.00, paid=False)
        auction_expired = Auction.objects.create(lot=lot_two, description='German Bayonet', 
            number_of_bids=4, time_starting=datetime.now(), time_ending='2020-01-15 16:10:10', 
            expired=False, winner=user, winning_bid=80.00, paid=False)
        auction.save()
        auction_expired.save()

    
    def test_all_lot_items_view_returns_correct_template(self):
        user = User.objects.get(pk=1)
        login_successful = self.client.login(username=user.username, password='addkj3245!')
        self.assertTrue(login_successful)

        response = self.client.get(reverse('all_lot_items'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lot_items.html')

           
    def test_lot_view_returns_correct_template(self):
        lot_obj = Lot.objects.get(id=1)

        response = self.client.get('/auctions/lot/{0}/'.format(lot_obj.id), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lot.html')
    

    def test_all_auctions_returns_correct_template(self):
        page = self.client.get('/auctions/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'auctions.html')
    
     
    def test_auction_returns_correct_template(self):
        auction = Auction.objects.get(id=1)

        response = self.client.get('/auctions/{0}/'.format(auction.id), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auction.html')


    def test_auction_expired_returns_correct_template(self):
        auction = Auction.objects.get(id=2)

        response = self.client.get('/auctions/{0}/'.format(auction.id), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auction_expired.html')
