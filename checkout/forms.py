from django import forms
from .models import Order, OrderLineItem


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(j, j) for j in range(2020, 2030)]

    credit_card_number = forms.CharField(
                                         label='Credit Card Number:',
                                         required=False,
                                         help_text="We only accept Visa")
    cvv = forms.CharField(
                          label='Security code (CVV): ',
                          required=False)
    expiry_month = forms.ChoiceField(
                                     label="Month",
                                     choices=MONTH_CHOICES,
                                     required=False)
    expiry_year = forms.ChoiceField(
                                    label='Year',
                                    choices=YEAR_CHOICES,
                                    required=False)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone', 'country', 'postcode',
                  'town_or_city', 'street_address')