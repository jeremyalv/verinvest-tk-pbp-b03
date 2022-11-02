from django import forms
from users.models import VerinvestUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import *


class RegisterForm(UserCreationForm):
    USER_TYPES = [('regular_user', 'Regular User'), ('domain_expert', 'Domain Expert')]
    form_input_class = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary focus:border-primary block w-full p-2.5'

    username = forms.CharField(label='Username', min_length=5, max_length=150,
                widget=forms.TextInput(
                    attrs={
                        'id': 'username',
                        'name': 'username',
                        'placeholder': 'johndoe',
                        'class': form_input_class
                    }
                ))

    user_type = forms.ChoiceField(label='Type', widget=forms.RadioSelect, choices=USER_TYPES)

    first_name = forms.CharField(label='First Name', empty_value='John', max_length=20,
                widget=forms.TextInput(
                    attrs={
                        'id': 'first_name',
                        'name': 'first_name',
                        'placeholder': 'John',
                        'class': form_input_class                 
                    }
                ))
    
    last_name = forms.CharField(label='Last name', empty_value='Doe', max_length=20,
                widget=forms.TextInput(
                    attrs={
                        'id': 'last_name',
                        'name': 'last_name',
                        'placeholder': 'Doe',
                        'class': form_input_class
                    }
                ))

    password1 = forms.CharField(label='Password', 
                widget=forms.PasswordInput(
                    attrs={
                        'placeholder': '•••••••••',
                        'class': form_input_class
                    }
                ))
    password2 = forms.CharField(label='Confirm Password', 
                widget=forms.PasswordInput(
                    attrs={
                        'placeholder': '•••••••••',
                        'class': form_input_class
                    }
                ))

    def username_clean(self):
        username = self.cleaned_data['username']
        users_count = VerinvestUser.objects.filter(username=username)

        if users_count.count():
            raise ValidationError('User already exist.')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords don\'t match!')
        return password2

    def save(self, commit=True):
        user = VerinvestUser.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user_type=self.cleaned_data['user_type'],
        )

        return user
    
        




