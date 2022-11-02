from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'is_expert']

    USER_TYPES = [('regular_user', 'Regular User'), ('domain_expert', 'Domain Expert')]
    form_input_class = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary focus:border-primary block w-full p-2.5'

    first_name = forms.CharField(label='First Name', empty_value='', max_length=20, required=True,
                widget=forms.TextInput(
                    attrs={
                        'id': 'first_name',
                        'name': 'first_name',
                        'placeholder': 'John',
                        'class': form_input_class                 
                    }
                ))
    last_name = forms.CharField(label='Last name', empty_value='', max_length=20, required=True,
                widget=forms.TextInput(
                    attrs={
                        'id': 'last_name',
                        'name': 'last_name',
                        'placeholder': 'Doe',
                        'class': form_input_class
                    }
                ))
    user_type = forms.ChoiceField(label='I am a...', widget=forms.RadioSelect, choices=USER_TYPES, required=True)
    email = forms.EmailField(label='Email address', empty_value='', required=True, 
                widget=forms.EmailInput(
                    attrs={
                        'id': 'email',
                        'name': 'email',
                        'placeholder': 'john.doe@email.com',
                        'class': form_input_class,
                    }
                ))

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.is_expert = True if self.cleaned_data['user_type'] == 'domain_expert' else False

        if commit:
            user.save()

        return user
    
        