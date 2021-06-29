from app.forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns = [
    #path('', views.home),
    #path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/>', views.mobile, name='mobile'),
    #path('login/', views.login, name='login'),
    #path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('accounts/login' , auth_views.LoginView.as_view(template_name='app/login.html' , authentication_form= LoginForm ), name='login'),
    #class based views
    path('' , views.ProductView.as_view() , name = 'home'),    
    path('product-detail/<int:pk>' , views.product_detail.as_view() , name = 'product-detail'),     
    path('registration/', views.customerregistration.as_view() , name='customerregistration')
]
