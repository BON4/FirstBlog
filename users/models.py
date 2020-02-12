from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
import django.dispatch

django.dispatch.Signal()


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, name, email, password, **kwargs):

        if not name:
            raise ValueError('Name must be provided')

        if not email:
            raise ValueError('Email address must be provided')

        if not password:
            raise ValueError('Password must be provided')

        email = self.normalize_email(email)
        user = self.model(name=name, email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name=None, email=None, password=None, **kwargs):
        return self._create_user(name, email, password, **kwargs)

    def create_superuser(self, name, email, password, **kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True

        return self._create_user(name, email, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'name'
    EMAIL_FIELD = 'email'

    objects = UserAccountManager()

    name = models.CharField('name', blank=True, max_length=200, unique=True)
    email = models.EmailField('email', unique=True, blank=False, null=False)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active status', default=True)
    is_verified = models.BooleanField('verified', default=False)
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    def get_class(self):
        return self.__class__

    def __str__(self):
        return str(self.name)

    def get_email(self):
        return self.email

    def __unicode__(self):
        return self.email

# Create your models here.
