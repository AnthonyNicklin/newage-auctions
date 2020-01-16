from django.urls import path

from .views import index, not_found, server_error

urlpatterns = [
    path('', index, name='index'),
    path('not_found/', not_found, name='not_found'),
    path('server_error/', server_error, name='server_error')
]