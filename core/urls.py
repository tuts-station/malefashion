from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from .views import RegisterView

urlpatterns = [
    url(r'^$',views.ProductView.as_view(), name='home'),
    # path('', views.ProductView.as_view(), name="home"),
    url(r'^about/$', views.about, name='about'),
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^contact-us/$', views.contact, name='contact'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^signup/$', RegisterView.as_view(), name='signup'),
    url(r'^login/$', views.login, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
