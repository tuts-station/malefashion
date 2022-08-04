from django.shortcuts import render
from django import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
from .models import Slider, Product,Catagory, Cart, FavouriteProduct
from django.db.models import Q
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
    totalitem = 0
    amount = 0
    shipping_amount = 70.0
    totalamount = 0
    products = Product.objects.all()

    # Favourites,_ = FavouriteProduct.objects.get_or_create(user=request.user)

    # product_in_favorites = None
    # if products in Favourites.product.all():
    #     product_in_favorites = True
    # else:
    #     product_in_favorites = False

    catagories = Catagory.objects.all()
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount+shipping_amount
    return render(request, 'fashion/shop.html',{ 'products': products ,'catagories':catagories,'totalitem':totalitem,'totalamount':totalamount}) 

def contact(request):
    return render(request, 'fashion/contact.html')

# @login_required()
def add_to_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    item_already_in_cart1 = False
    product = request.GET.get('prod_id')
    item_already_in_cart1 = Cart.objects.filter(Q(product=product) & Q(user=request.user)).exists()
    if item_already_in_cart1 == False:
        product_title = Product.objects.get(id=product)
        Cart(user=user, product=product_title).save()
        return redirect('/cart')
    else:
        return redirect('/cart')

# @login_required
def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        totalamount=0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                # print(p.product.discounted_price)
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            totalamount = amount+shipping_amount
            return render(request, 'fashion/cart.html', {'carts':cart, 'amount':amount, 'totalamount':totalamount, 'totalitem':totalitem})
        else:
            return render(request, 'fashion/emptycart.html', {'totalitem':totalitem})
    else:
        return render(request, 'fashion/emptycart.html', {'totalitem':totalitem})

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount= 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        data = {
            'prod_id':prod_id,
            'amount':amount,
            'totalamount':amount+shipping_amount
        }
        return JsonResponse(data)
    else:
        return HttpResponse("")

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount= 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            # print("Quantity", p.quantity)
            # print("Selling Price", p.product.discounted_price)
            # print("Before", amount)
            amount += tempamount
            # print("After", amount)
        # print("Total", amount)
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shipping_amount
        }
        return JsonResponse(data)
    else:
        return HttpResponse("")

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount= 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            # print("Quantity", p.quantity)
            # print("Selling Price", p.product.discounted_price)
            # print("Before", amount)
            amount += tempamount
            # print("After", amount)
        # print("Total", amount)
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shipping_amount
        }
        return JsonResponse(data)
    else:
        return HttpResponse("")

def Favorites(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user
    Favourites,_ = FavouriteProduct.objects.get_or_create(user=user)

    product = Product.objects.get(id=id)

    print('if')
    if product not in Favourites.product.all():
        Favourites.product.add(product)
        data = {
            'product':True
        }
        return JsonResponse(data)
    else:
        print('else')
        Favourites.product.remove(product)
    
    Favourites.save()
    # messages.success(request, 'Product Add to Favourite Successfully!')
    return HttpResponse('Success')

def favoritesPage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    FavProducts,_ = FavouriteProduct.objects.get_or_create(user=user)
    # print(FavProducts.product.all())
    return render(request, 'fashion/favourites.html', { 'product_list': FavProducts.product.all(), "favorites": True})

def checkout(request):
    return render(request, 'fashion/checkout.html')

class productDetails(View):
    def get(self, request, pk):
        totalitem = 0
        product = Product.objects.get(pk=pk)

        Favourites,_ = FavouriteProduct.objects.get_or_create(user=request.user)

        product_in_favorites = None
        if product in Favourites.product.all():
            product_in_favorites = True
        else:
            product_in_favorites = False

        item_already_in_cart=False

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'fashion/proDetails.html', {'product':product,'totalitem':totalitem,'product_in_favorites':product_in_favorites})

def userProfile(request):
    return render(request, 'fashion/userProfile.html')

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