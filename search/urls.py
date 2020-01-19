from django.urls import path

from .views import keyword_search, category


urlpatterns = [
    path('', keyword_search, name='keyword_search'),
    path('<str:category>', category, name='category'),
]