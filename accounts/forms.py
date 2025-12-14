from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email address'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Password fields (because they come from UserCreationForm)
        self.fields['password1'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Password'
        }

        self.fields['password2'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Confirm password'
        }

      