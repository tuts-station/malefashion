from django.shortcuts import render
from django import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,logout,authenticate,get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.hashers import make_password, check_password
from .forms import RegisterForm, LoginForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView,TemplateView

# Create your views here.

class ProductView(View):
    def get(self, request):
        return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')    

def shop(request):
    return render(request, 'core/shop.html') 

def contact(request):
    return render(request, 'core/contact.html')

def cart(request):
    return render(request, 'core/cart.html')

def checkout(request):
    return render(request, 'core/checkout.html')

# def signup(request):
#     return render(request, 'core/signup.html')

# def login(request):
#     return render(request, 'core/login.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'core/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            messages.success(request, 'User created Successfully!')
            new_user = authenticate(email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )
            auth_login(request, new_user)
            return redirect('')
        else:
            messages.warning(request, 'Oops! something went wrong!')

        return render(request, self.template_name, {'form': form})

def login(request):
    form = LoginForm(request.POST or None)

    if not request.user.is_authenticated:
        if request.method == "POST":

            if form.is_valid():
                user = authenticate(email=request.POST.get("email"), password=request.POST.get("password1"))
                print(user)
                if user is not None:
                    login(request, user)
                    return redirect('')
                else:
                    messages.warning(request, 'Invalid credentials!')
            else:
                messages.warning(request, 'Oops! something went wrong!')
        return render(request, "core/login.html", {"form": form})
    return redirect("")