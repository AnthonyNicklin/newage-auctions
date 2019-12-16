from django.contrib.auth.models import User


class EmailAuth:
    """ Authentication by email """

    def authenticate(self, username=None, password=None):
        """ Get an instance of 'User' based off the email and verify
        the password """

        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        """ Used by django auth to get user instance """

        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None