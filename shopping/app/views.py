from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .models import *
from .forms import *
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        topwear = Product.objects.filter(category = 'TW')
        bottomwear = Product.objects.filter(category = 'BW')
        mobile = Product.objects.filter(category = 'M')
        laptop = Product.objects.filter(category = 'L')

        context = {'topwear' : topwear , 'bottomwear' : bottomwear , 'mobile' : mobile , 'laptop' : laptop}

        return render(request , 'app/home.html' , context)


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class product_detail(View):
    def get(self, request , pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html' , {'product' : product})


def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    if(data == None):
        mobiles= Product.objects.filter(category= 'M')
    elif(data== 'Redmi' or data== 'samsung'):
        mobiles= Product.objects.filter(category= 'M').filter(brand=data)
    return render(request, 'app/mobile.html' , {'mobiles' :mobiles})

def login(request):
 return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class customerregistration(View):
    def get(self, request):
        form= CustomerRegistrationForm()
        context = {'form' : form}
        return render(request, 'app/customerregistration.html' , context )
    def post(self, request):
        form= CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account has been registered!!')
            form.save()
            return render(request, 'app/login.html')
        else:
            context = {'form' : form}
            return render(request, 'app/customerregistration.html' , context )
        


def checkout(request):
 return render(request, 'app/checkout.html')
