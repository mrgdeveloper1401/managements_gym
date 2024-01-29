from django.contrib.auth.models import BaseUserManager


class UsersManager(BaseUserManager):
    def create_user(self, username, email, mobile_phone, first_name, last_name, password=None):
        if not username:
            raise ValueError('username must be set')
        if not email:
            raise ValueError('email must be set')
        if not first_name:
            raise ValueError('first name must be set')
        if not last_name:
            raise ValueError('last name must be set')
        if not mobile_phone:
            raise ValueError('mobile phone must be set')
        user = self.model(username=username, email=self.normalize_email(email), first_name=first_name, last_name=last_name,
                          mobile_phone=mobile_phone)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, mobile_phone, first_name, last_name, password=None):
        user = self.create_user(username=username, email=email, first_name=first_name, last_name=last_name,
                                password=password, mobile_phone=mobile_phone)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
