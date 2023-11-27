from django import forms
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password

from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password', 'class': 'form-control'
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )


class UserProfileForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Password', 'class': 'form-control'
        })
    )

    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    phone_number = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(UserProfileForm, self).clean()

        # Check if the password is provided
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # If password is not provided, remove it from the cleaned_data
        if not password:
            del cleaned_data['password']
            del cleaned_data['confirm_password']
        elif password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please enter matching passwords.")

        return cleaned_data

    def save(self, commit=True):
        instance = super(UserProfileForm, self).save(commit=False)

        # If a password is provided, hash it using Django's make_password
        if self.cleaned_data.get('password'):
            instance.password = make_password(self.cleaned_data['password'])
        if commit:
            instance.save()

        return instance
