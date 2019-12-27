from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from .models import Profile
from auction.models import Bid


def index(request):
    """ Return index.html file """
    
    return render(request, 'index.html')


@login_required
def logout(request):
    """ Logout users """

    auth.logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """ Return login page """

    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


@transaction.atomic
def registration(request):
    """ Render the registration page """

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.refresh_from_db()
            profile_form = ProfileForm(request.POST, instance=user.profile)
            profile_form.save()
    
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
        
            if user: 
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registered')
                return render(request, 'index.html')
            else:
                messages.error(request, 'Unable to register your account')
    else:
        form = UserRegistrationForm()
        profile_form = ProfileForm()
        

    context = {
        'form': form,
        'profile_form': profile_form
    }

    return render(request, 'registration.html', context)


@login_required
def user_profile(request):
    """ Returns the Users profile page """

    user = get_object_or_404(User, id=request.user.pk)
    user_bids = get_list_or_404(Bid, user_id=request.user.pk)

    context = {
        'user': user,
        'user_bids': user_bids
    }

    return render(request, 'profile.html', context)
