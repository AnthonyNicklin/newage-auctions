from django.urls import path, include

from .views import all_auctions, auction, bid, all_lot_items, lot

urlpatterns = [
    path('', all_auctions, name='all_auctions'),
    path('<int:auction_id>/', auction, name='auction'),
    path('<int:auction_id>/bid', bid, name='bid'),
    path('lots', all_lot_items, name='all_lot_items'),
    path('lot/<int:lot_id>/', lot, name='lot'),
]