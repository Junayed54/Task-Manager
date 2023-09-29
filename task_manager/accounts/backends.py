# myapp/auth_backends.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class MyCustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
