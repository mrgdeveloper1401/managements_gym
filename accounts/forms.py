from django import forms
from .models import Users


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'username', 'email', 'mobile_phone', 'password')


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'username', 'email', 'mobile_phone')
