from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django import forms
from . models import Record

# Register/ Create a User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


#  Login a user


class LoginForm(AuthenticationForm):
    username = forms.ChoiceField(widget=TextInput)
    password = forms.ChoiceField(widget=PasswordInput)


# class AddRecordForm(forms.ModelForm):
#     class Meta:
#         model = Record
#         fields = ['username', 'password1', 'password2']


#! - Create a recordd
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name',
                  'email', 'Phone', 'address', 'city', 'province', 'country']


#!  - Update Record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name',
                  'email', 'Phone', 'address', 'city', 'province', 'country']
