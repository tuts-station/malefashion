from django.urls import path
from core import views
from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static
from .views import RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    re_path(r'^$',views.ProductView.as_view(), name='home'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^shop/$', views.shop, name='shop'),
    re_path(r'^contact-us/$', views.contact, name='contact'),
    re_path(r'^cart/$', views.cart, name='cart'),
    re_path(r'^checkout/$', views.checkout, name='checkout'),
    re_path(r'^signup/$', RegisterView.as_view(), name='signup'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^product-details/$', views.productDetails, name='productDetails'),
    path("logout/", LogoutView.as_view(), name="logout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
