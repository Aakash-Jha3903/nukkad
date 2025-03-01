"""
URL configuration for Ecommerce_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # for media files
from django.conf.urls.static import static  # for media files
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('404', views.Error404, name='404'),

    path('', views.HOME, name='home'),
    path('about', views.About, name='about'),
    path('contact', views.Contact, name='contact'),

    path('product', views.Product_Page, name='product'),
    path('product/filter-data', views.filter_data, name="filter-data"),
    path('product/<slug:slug>', views.Product_Details, name='product_detail'),

    # path('account/my_account',views.MyAccount,name='my_account'),
    path('account/register', views.Register, name='handleregister'),
    path('account/login', views.Login, name='handlelogin'),
    path('account/profile', views.Profile, name='profile'),
    path('account/profile/update', views.Profile_Update, name='profile_update'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # for media files
