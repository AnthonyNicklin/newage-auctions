from django.shortcuts import get_object_or_404

from auction.models import Auction


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    
    for id, quantity in cart.items():
        auction = get_object_or_404(Auction, pk=id)
        total += quantity * auction.buy_now
        cart_items.append({'id': id, 'quantity': quantity, 'auction': auction})
    
    return ({'cart_items': cart_items, 'total': total})