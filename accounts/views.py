from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegistrationForm, UserDetailsRegistration
from .models import UserDetails


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
            user = auth.authenticate(username=request.POST['username'],
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


def registration(request):
    """ Render the registration page """

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
         
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registered')
            else:
                messages.error(request, 'Unable to register your account')
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {'registration_form': registration_form})


@login_required
def user_profile(request):
    """ Returns the Users profile page """

    user = get_object_or_404(User, id=request.user.pk)

    if request.method == 'POST':
        user_details_form = UserDetailsRegistration(request.POST, instance=request.user)

        if user_details_form.is_valid():
            user_details = UserDetails()
            user_details.user_id = user
            user_details_form.save()
            messages.success(
                request,
                f'Your account has been successfully updated')
            return redirect('profile')
    else:
        user_details_form = UserDetailsRegistration(instance=request.user)

    context = {
        'profile': user,
        'user_details_form': user_details_form,
    }

    return render(request, 'profile.html', context)