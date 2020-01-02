from django.test import TestCase

from accounts.forms import UserRegistrationForm, ProfileForm


class TestUserForm(TestCase):

    def test_can_create_a_user(self):
        form = UserRegistrationForm({'fist_name': 'John',
                                    'last_name': 'Smith',
                                    'username': 'user3',
                                    'email': 'john.smith@gmail.com',
                                    'password1': 'testpassword1234',
                                    'password2': 'testpassword1234'})
        self.assertTrue(form.is_valid())


    def test_can_create_profile(self):
        form = ProfileForm({'phone': '0123456789',
                            'address': '5 Downshire Road',
                            'town': 'Johnstown',
                            'postcode': 'BY67 7HJ',
                            'country': 'Ireland'})
        self.assertTrue(form.is_valid())


