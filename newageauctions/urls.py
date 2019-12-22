"""newageauctions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
from django.views import static
from .settings import MEDIA_ROOT

from home.views import index
#from home import urls as home_urls
from accounts.urls import urlpatterns as accounts_urls
from cart.urls import urlpatterns as cart_urls
from checkout.urls import urlpatterns as checkout_urls
from auction.urls import urlpatterns as auction_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include(accounts_urls)),
    path('auctions/', include(auction_urls)),
    path('cart/', include(cart_urls)),
    path('checkout/', include(checkout_urls)),
    path('media/(?Ppath.*)', static.serve,{'document_root': MEDIA_ROOT}),
]