from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #first_name = forms.CharField(max_length=64)
    #last_name = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ['username',
                  'email', 'password1', 'password2']


class loginRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class User_Update_Form(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
