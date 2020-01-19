from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import logout, login, registration, user_profile, bid_history, delete_account


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', registration, name='registration'),
    path('profile/', user_profile, name='profile'),
    path('bid_history/', bid_history, name='bid_history'),
    path('delete-account/', delete_account, name='delete_account' ),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('change-password/done', auth_views.PasswordChangeDoneView.as_view()),
    path('password-reset/', auth_views.PasswordResetView.as_view()),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view()),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view()),
]
