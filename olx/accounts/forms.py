from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta():
        model1 = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

