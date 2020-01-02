from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.shortcuts import reverse

from accounts.views import registration


class TestAccountsViews(TestCase):
    @classmethod
    # Set up non-modified objects used by all test methods
    def setUpTestData(cls):
        User.objects.create_user(username='Peter', email='pete.polo@gmail.com', password='addkj3245!')

    
    def test_index_view_returns_correct_template(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')


    def test_register_view_returns_correct_template(self):
        page = self.client.get('/accounts/register/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration.html')


    def test_registration_function(self):
        page = self.client.get('/accounts/register/')
        user = User.objects.get(pk=1)
        self.assertEqual(page.status_code, 200)
        self.assertTrue(user)


    def test_login_view_returns_correct_template(self):
        page = self.client.get('/accounts/login/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')


    def test_login_view(self):
        user = User.objects.get(pk=1)
        login_successful = self.client.login(username=user.username, password='addkj3245!')
        self.assertTrue(login_successful)

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


    def test_profile_view_returns_correct_template(self):
        user = User.objects.get(pk=1)
        login_successful = self.client.login(username=user.username, password='addkj3245!')
        self.assertTrue(login_successful)

        page = self.client.get('/accounts/profile')
        self.assertEqual(page.status_code, 301)
        self.assertTemplateUsed(reverse('profile'))
        
    
        
    