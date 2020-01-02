from django.test import TestCase
from django.contrib.auth.models import User

from accounts.models import Profile


class TestAccountModels(TestCase):
    

    def test_user_model(self):
        username = User.objects.create_user(
            username='John12', email='john.smith@gmail.com', password='akdf34983!',
            first_name='John', last_name='Smith'
        )
        username.save()
        self.assertEqual(str(username), 'John12')


    