from django.urls import path

from .views import all_auctions, auction, bid, all_lot_items, lot, category, lot_sold

urlpatterns = [
    path('', all_auctions, name='all_auctions'),
    path('<int:auction_id>/', auction, name='auction'),
    path('<int:auction_id>/bid', bid, name='bid'),
    path('lots', all_lot_items, name='all_lot_items'),
    path('lot/<int:lot_id>/', lot, name='lot'),
    path('<str:category>', category, name='category'),
    path('lot_sold/<int:auction_id>/', lot_sold, name='lot_sold'),
]