from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class EmailBackend(BaseBackend):
    def authenticate(self, username=None, password = None, **kwargs) -> None:
        Users = get_user_model()
        try:
            user = Users.objects.get(Q(email=username))
        except Users.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user;
        return None

    def get_user(self, user_id) -> None:
        Users = get_user_model()
        try:
            return Users.objects.get(pk =user_id)
        except:
            return None