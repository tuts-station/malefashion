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
from django.contrib.auth import login, logout,authenticate,get_user_model
from django.contrib.auth import login as auth_login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.hashers import make_password, check_password
from .forms import RegisterForm, LoginForm
from django.views import View
from .models import Slider, Product,Catagory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView,TemplateView

# Create your views here.

class ProductView(View):
    def get(self, request):
        sliders = Slider.objects.all()
        return render(request, 'fashion/home.html',{ 'sliders': sliders })

def about(request):
    return render(request, 'fashion/about.html')    

def shop(request):
    products = Product.objects.all()
    catagories = Catagory.objects.all()
    return render(request, 'fashion/shop.html',{ 'products': products ,'catagories':catagories}) 

def contact(request):
    return render(request, 'fashion/contact.html')

def cart(request):
    return render(request, 'fashion/cart.html')

def checkout(request):
    return render(request, 'fashion/checkout.html')

def productDetails(request):
    return render(request, 'fashion/proDetails.html')

def userProfile(request):
    return render(request, 'fashion/userProfile.html')

# def signup(request):
#     return render(request, 'fashion/signup.html')

# def login(request):
#     return render(request, 'fashion/login.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'fashion/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(email=email, password=raw_password)

            messages.success(request, 'User created Successfully!')
            return redirect('login')
        else:
            messages.warning(request, 'Oops! something went wrong!')

        return render(request, self.template_name, {'form': form})

def login(request):
    form = LoginForm(request.POST or None)

    if not request.user.is_authenticated:
        if request.method == "POST":

            if form.is_valid():
                user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
                if user is not None:
                    auth_login(request, user)
                    return redirect('home')
                else:
                    messages.warning(request, 'Invalid credentials!')
            else:
                messages.warning(request, 'Oops! something went wrong!')
        return render(request, "fashion/login.html", {"form": form})
    return redirect("")