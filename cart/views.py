from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from auction.models import Auction


@login_required
def view_cart(request):
    """A View that renders the cart contents page"""

    user = auth.get_user(request)
    auctions = Auction.objects.all()
    cart = []

    for auction in auctions:
        if user == auction.winner and auction.paid == False:
            cart.append({'auction': auction})

    context = {
        'cart': cart
    }
    return render(request, "cart.html", context)


@login_required
def remove_from_cart(request, auction_id):
    """ Remove auction from cart """

    auction = get_object_or_404(Auction, pk=auction_id)
    user_default = get_object_or_404(User, pk=1)

    if auction:
        auction.winner = user_default
        auction.save()
        messages.success(request, '{0} was removed from the cart'.format(auction_id))
        return redirect('view_cart')
    else:
        messages.error(request, 'Sorry we are unable remove this form your cart')
        return redirect('view_cart')
