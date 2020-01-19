from django.db import models

from auction.models import Auction


class Order(models.Model):

    full_name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address = models.CharField(max_length=40, blank=False)
    date = models.DateTimeField()
    payment_id = models.CharField(max_length=250, default="00000")

    def __str__(self):
        return "{0}: {1} {2}".format(self.pk, self.date, self.full_name.title())


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.auction.pk)