from django.urls import path

from .views import keyword_search_lots, category, keyword_search_auctions


urlpatterns = [
    path('lots', keyword_search_lots, name='keyword_search_lots'),
    path('auctions', keyword_search_auctions, name='keyword_search_auctions'),
    path('<str:category>', category, name='category'),
]