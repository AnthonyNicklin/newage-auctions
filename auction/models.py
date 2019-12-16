from django.db import models
from django.contrib.auth.models import User

class Lot(models.Model):
    """ Lot object """

    MILITARY = 'MIL'
    REAL_ESTATE = 'RLE'
    WEAPONS = 'WEA'
    CULTURAL = 'CUL'
    NONE = 'NUL'
    CATEGORIES = (
        (NONE, 'Select a category'),
        (MILITARY, 'Military'),
        (REAL_ESTATE, 'Real Estate'),
        (WEAPONS, 'Weapons'),
        (CULTURAL, 'Cultural')
    )

    name = models.CharField(max_length=200, blank=False)
    origin = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    age = models.IntegerField(blank=False)
    image = models.ImageField()
    category = models.CharField(max_length=3, choices=CATEGORIES, blank=False)
    date_added = models.DateField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name_plural = 'lot items'

    def __str__(self):
        """ Return a string of the model """

        return "Lot " + str(self.pk)


class Auction(models.Model):
    """ Auction object """

    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    number_of_bids = models.IntegerField(default=0)
    buy_now = models.IntegerField(default=0)
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Auctions"

    def __str__(self):
        """ Return a string of the model """

        return "Auction " + str(self.pk)


class Bid(models.Model):
    """ Bid object """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    bid_time = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Bids'

    def __str__(self):
        """ Return a string of the model """

        return "Bid " + str(self.pk)

