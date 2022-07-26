from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
            }
        ),error_messages={'required': 'The Email is required.'})
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
            }
        ),error_messages={'required': 'The Password is required.'})

# class UserUpdateForm(UserCreationForm):
#     username = forms.CharField(max_length=100,
#                                required=True,
#                                widget=forms.TextInput(attrs={'placeholder': 'Username',
#                                                              'class': 'form-control',
#                                                              }),
#                                error_messages={'required': 'The Username is required.'})
#     email = forms.EmailField(required=True,
#                              widget=forms.TextInput(attrs={'placeholder': 'Email',
#                                                            'class': 'form-control',
#                                                            }),
#                              error_messages={'required': 'The Email is required.'})
#     password1 = forms.CharField(max_length=50,
#                                 required=False,
#                                 widget=forms.PasswordInput(attrs={'placeholder': 'Password',
#                                                                   'class': 'form-control',
#                                                                   'data-toggle': 'password',
#                                                                   'id': 'password',
#                                                                   }))
#     password2 = forms.CharField(max_length=50,
#                                 required=False,
#                                 widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
#                                                                   'class': 'form-control',
#                                                                   'data-toggle': 'password',
#                                                                   'id': 'password',
#                                                                   }))

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             'username',  
#             'email', 
#             'first_name', 
#             'last_name', 
#             'password',
#         ]

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = [
#             'profile_image'
#         ]