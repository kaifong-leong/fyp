
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

# -- Create/Register a user (Model Form)

class CreateUserForm(UserCreationForm): # inherit from UserCreationForm and then edit

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] # choose the fields we want, 2 fields for password to re-enter the same password


# -- Authenticate a user (Model Form)

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

