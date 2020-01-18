from django.urls import path

from .views import checkout, payment_successful, cancel_payment

urlpatterns = [
    path('', checkout, name='checkout'),
    path('payment-success', payment_successful, name='payment_successful'),
    path('cancel-payment', cancel_payment, name='cancel_payment'),
]