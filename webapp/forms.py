from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django import forms


# Register/ Create a User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


#  Login a user


class LoginForm(AuthenticationForm):
    username = forms.ChoiceField(widget=TextInput)
    password = forms.ChoiceField(widget=PasswordInput)
