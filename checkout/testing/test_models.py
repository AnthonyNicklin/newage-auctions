from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime

from checkout.models import Order
from auction.models import Lot, Auction


class OrderModelTest(TestCase):
    """ Tests fot the Order model """
    @classmethod
    # Set up non-modified objects used by all test methods
    def setUpTestData(cls):
        Order.objects.create(id=1, full_name='John Smith', phone='012345789', 
            country="Ireland", postcode='BD90 0IK', town_or_city='Johns Town',
            street_address='4 Brookman Road', date=datetime.now(),
            payment_id='cdfe343sdfv3464533d')

    def test_full_name_label(self):
        order_obj = Order.objects.get(id=1)
        field_label = order_obj._meta.get_field('full_name').verbose_name
        self.assertEquals(field_label, 'full name')

    def test_full_name_max_length(self):
        order_obj = Order.objects.get(id=1)
        max_length = order_obj._meta.get_field('full_name').max_length
        self.assertEquals(max_length, 50)

    def test_phone_label(self):
        order_obj = Order.objects.get(id=1)
        field_label = order_obj._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    def test_phone_max_length(self):
        order_obj = Order.objects.get(id=1)
        max_length = order_obj._meta.get_field('phone').max_length
        self.assertEquals(max_length, 20)

    def test_country_label(self):
        order_obj = Order.objects.get(id=1)
        field_label = order_obj._meta.get_field('country').verbose_name
        self.assertEquals(field_label, 'country')
    
    def test_country_max_length(self):
        order_obj = Order.objects.get(id=1)
        max_length = order_obj._meta.get_field('country').max_length
        self.assertEquals(max_length, 40)

    def test_postcode_label(self):
        order_obj = Order.objects.get(id=1)
        field_label = order_obj._meta.get_field('postcode').verbose_name
        self.assertEquals(field_label, 'postcode')
    
    def test_postcode_max_length(self):
        order_obj = Order.objects.get(id=1)
        max_length = order_obj._meta.get_field('postcode').max_length
        self.assertEquals(max_length, 20)

    def test_town_or_city_label(self):
        order_obj = Order.objects.get(id=1)
        field_label = order_obj._meta.get_field('town_or_city').verbose_name
        self.assertEquals(field_label, 'town or city')
    
    def test_town_or_city_max_length(self):
        order_obj = Order.objects.get(id=1)
        max_length = order_obj._meta.get_field('town_or_city').max_length
        self.assertEquals(max_length, 40)

    def test_street_address_label(self):
        order_obj = Order.objects.get(id=1)
        field_label = order_obj._meta.get_field('street_address').verbose_name
        self.assertEquals(field_label, 'street address')
    
    def test_street_address_max_length(self):
        order_obj = Order.objects.get(id=1)
        max_length = order_obj._meta.get_field('street_address').max_length
        self.assertEquals(max_length, 40)

    def test_payment_id_label(self):
        order_obj = Order.objects.get(id=1)
        field_label = order_obj._meta.get_field('payment_id').verbose_name
        self.assertEquals(field_label, 'payment id')
    
    def test_payment_id_max_length(self):
        order_obj = Order.objects.get(id=1)
        max_length = order_obj._meta.get_field('payment_id').max_length
        self.assertEquals(max_length, 250)
    
    def test_date_label(self):
        order_obj = Order.objects.get(id=1)
        field_label = order_obj._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'date')

