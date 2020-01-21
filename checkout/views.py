import os
import stripe
from datetime import datetime

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import timezone
from django.contrib import messages, auth

from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from auction.models import Auction

stripe.api_key = os.environ.get('STRIPE_SECRET')
STRIPE_PUBLISHABLE = os.environ.get('STRIPE_PUBLISHABLE')


@login_required()
def checkout(request):

    user = auth.get_user(request)
    auctions = Auction.objects.filter(winner=user).filter(paid=False)
    total = 0 

    for auction in auctions:
        total += auction.winning_bid

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=user.email,
                    source="tok_visa",
                    receipt_email=user.email
                    
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                order = order_form.save(commit=False)
                order.date = datetime.now()
                order.payment_id = customer.id
                order.save()

                for auction in auctions:
                    order_line_item = OrderLineItem(
                        order=order,
                        auction=auction,
                    )
                    order_line_item.save()
                    auction.paid = True
                    auction.save()
                messages.success(request, "You have successfully paid")
                return redirect(reverse('all_auctions'))
            else:
                messages.error(request, "Unable to take payment") 
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    context = {
        "order_form": order_form,
        "payment_form": payment_form,
        "pk": STRIPE_PUBLISHABLE,
        "total": total
    }
    
    return render(request, "checkout.html", context)

