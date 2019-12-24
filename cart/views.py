from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from auction.models import Auction


def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    
    quantity = 1
    cart = request.session.get('cart', {})
    if id in cart:
        messages.info(request, 'You already have this item in your cart')     
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = 1
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, id):
    """ Remove items from cart """

    auction = get_object_or_404(Auction, pk=id)
    cart = request.session.get('cart', {})

    del cart[id]
    request.session['cart'] = cart
    messages.success(request, '{0} was removed from the cart'.format(auction.lot.name))
    return redirect('view_cart')
