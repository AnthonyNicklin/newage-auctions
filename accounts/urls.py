from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile
from accounts import urls_reset

urlpatterns = [
      url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', registration, name='registration'),
    url(r'^profile/$', user_profile, name='profile'),
    url(r'^password_reset/', include(urls_reset))
]