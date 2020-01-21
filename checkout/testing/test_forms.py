from django.test import TestCase

from checkout.forms import MakePaymentForm, OrderForm


class TestMakePaymentForm(TestCase):
    """ Test MakePaymentForm """

    def test_can_make_payment(self):
        form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'cvv': '235',
            'expiry_month': 12,
            'expiry_year': '2022',

        })
        self.assertTrue(form.is_valid())


class TestOrderForm(TestCase):
    """ Test for OrderForm """

    def test_order_form(self):
        form = OrderForm({
            'full_name': 'John Smith',
            'phone': '0123456789',
            'country': 'England',
            'postcode': 'KL87 6HY',
            'town_or_city': 'Johns Town',
            'street_address': '0 Browns Ave'
        })
        self.assertTrue(form.is_valid())