from django.contrib import admin

from .models import Auction, Lot, Bid


class BidAdmin(admin.ModelAdmin):

    readonly_fields = (
        'user',
        'auction',
        'bid_amount', 
        'bid_time',
    )
    

admin.site.register(Auction)
admin.site.register(Lot)
admin.site.register(Bid, BidAdmin)
