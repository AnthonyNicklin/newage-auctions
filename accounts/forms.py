from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Profile


class UserLoginForm(forms.Form):
    """Form for user login """

    username = forms.CharField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """ Form used to register new user """

    password1 = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation", 
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'username', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")

        if password1 != password2:
            raise ValidationError("Passwords must match")

        return password2


class ProfileForm(forms.ModelForm):

    phone = forms.CharField(max_length=11, label="Phone")                                                                                                                                                                                                                                                                             
    address = forms.CharField(max_length=255, label="Address")
    town = forms.CharField(max_length=45, label="Town")
    postcode = forms.CharField(max_length=45, label="Postcode")
    country = forms.CharField(max_length=45, label="Country")

    class Meta:
        model = Profile
        fields = ['phone', 'address', 'town', 'postcode', 'country']

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        return phone

    def clean_address(self):
        address = self.cleaned_data['address']

        return address

    def clean_town(self):
        town = self.cleaned_data['town']

        return town

    def clean_postcode(self):
        postcode = self.cleaned_data['postcode']

        return postcode

    def clean_country(self):
        country = self.cleaned_data['country']

        return country


class UpdateUserForm(forms.ModelForm):
    """ Update user details """

    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]


class UpdateProfileForm(forms.ModelForm):
    """ Update the user details """

    phone = forms.CharField(max_length=11, label="Phone")                                                                                                                                                                                                                                                                             
    address = forms.CharField(max_length=255, label="Address")
    town = forms.CharField(max_length=45, label="Town")
    postcode = forms.CharField(max_length=45, label="Postcode")
    country = forms.CharField(max_length=45, label="Country")

    class Meta:
        model = Profile
        fields = ['phone', 'address', 'town', 'postcode', 'country']

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        return phone

    def clean_address(self):
        address = self.cleaned_data['address']

        return address

    def clean_town(self):
        town = self.cleaned_data['town']

        return town

    def clean_postcode(self):
        postcode = self.cleaned_data['postcode']

        return postcode

    def clean_country(self):
        country = self.cleaned_data['country']

        return country
