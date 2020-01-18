from django.urls import path

from .views import checkout, checkout

urlpatterns = [
    path('checkout', checkout, name="checkout")
]