from django.conf.urls import url

from .views import all_auctions, auction, bid, all_lot_items, lot

urlpatterns = [
    url(r'^$', all_auctions, name='all_auctions'),
    url(r'^(?P<auction_id>\d+)/$', auction, name='auction'),
    url(r'^(?P<auction_id>\d+)/bid$', bid, name='bid'),
    url(r'^lots', all_lot_items, name='all_lot_items'),
    url(r'^lot/(?P<lot_id>\d+)/$', lot, name='lot'),
]