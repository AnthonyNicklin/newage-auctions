from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import UserLoginForm, UserRegistrationForm, ProfileForm, UpdateUserForm, UpdateProfileForm, ChangePassword
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
    return redirect('login')


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
    """ Update user profile """

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Invalid form submitted')
            return render(request, 'profile.html')
    else:
        form = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'form': form,
        'profile_form': profile_form
    }

    return render(request, 'profile.html', context)


@login_required
def bid_history(request):
    """ Render the bidding history for the user """

    bid_obj = Bid.objects.filter(user=request.user.pk).order_by('-bid_time')
    paginator = Paginator(bid_obj, 25)

    page = request.GET.get('page')
    try:
        bid_items = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver first page.
        bid_items = paginator.page(1)
    except EmptyPage:
        # If page is not an integer, deliver first page.
        bid_items = paginator.page(paginator.num_pages)

    return render(request, 'bid_history.html', {'bid_items': bid_items})


@login_required
def delete_account(request):
    """ Delete User account """

    try:
        user = auth.get_user(request)
        user.delete()
        messages.success(request, 'Your account has been deleted')
        
        return redirect('index')
    except User.DoesNotExist:
        messages.error(request, 'User does not exist')

        return redirect('login')


