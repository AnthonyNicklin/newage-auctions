from django.test import TestCase
from django.contrib.auth.models import User


class CartViewTest(TestCase):
    @classmethod
    # Set up non-modified objects used by all test methods
    def setUpTestData(cls):

        user = User.objects.create_user(username='Peter', email='pete.polo@gmail.com', password='addkj3245!')
        user.save()


    def test_cart_view_returns_correct_template(self):
        user = User.objects.get(pk=1)
        login_successful = self.client.login(username=user.username, password='addkj3245!')
        self.assertTrue(login_successful)

        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')