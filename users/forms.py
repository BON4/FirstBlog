from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']


# алидатор при ходе в аккаунт
class UserAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError('There was a problem with your login.', code='invalid_login')
        elif not user.is_verified:
            raise forms.ValidationError('You must verify your account.', code='invalid_login')
