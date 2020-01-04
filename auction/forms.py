from django import forms

from .models import Bid


class BidForm(forms.ModelForm):
    """ Form to submit bid """

    bid_amount = forms.DecimalField(max_digits=9, decimal_places=2, 
        label='bid_amount')

    class Meta:
        model = Bid
        fields = ['bid_amount']



