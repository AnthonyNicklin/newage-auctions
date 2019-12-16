from django.contrib import admin

from .models import Auction, Lot, Bid

admin.site.register(Auction)
admin.site.register(Lot)
admin.site.register(Bid)
