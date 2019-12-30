from django.urls import path

from .views import view_cart, remove_from_cart


urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('remove_from_cart/<int:auction_id>/', remove_from_cart, name='remove_from_cart'),
]
