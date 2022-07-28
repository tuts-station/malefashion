from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             }),
                               error_messages={'required': 'The Username is required.'})
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           }),
                             error_messages={'required': 'The Email is required.'})
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'id': 'password',
                                                                  }),
                                error_messages={'required': 'The Password is required.'})
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'id': 'password',
                                                                  }),
                                error_messages={'required': 'The Confirm Password is required.'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
            }
        ),error_messages={'required': 'The Username is required.'})
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
            }
        ),error_messages={'required': 'The Password is required.'})

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email'}),error_messages={'required': 'The Email is required.'})

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),error_messages={'required': 'The Password is required.'}, help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),error_messages={'required': 'The Confirn Password is required.'},)

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus':True}),error_messages={'required': 'The Current Password is required.'})
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),error_messages={'required': 'The New Password is required.'}, help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),error_messages={'required': 'The New Password is required.'})