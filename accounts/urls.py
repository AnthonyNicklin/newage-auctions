from django.urls import path, include
from accounts.views import logout, login, registration, user_profile
from accounts import urls_reset

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', registration, name='registration'),
    path('profile/', user_profile, name='profile'),
    path('password_reset/', include(urls_reset))
]