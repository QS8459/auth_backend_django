from django.contrib.auth.models import BaseUserManager;


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Email field is required')
        email = self.normalize_email(email)
        user = self.model(email = email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user;

    def create_superuser(self, email, password = True, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True);
        return self.create_user(email, password, **kwargs)

