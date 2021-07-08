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


class product_detail(View):
    def get(self, request , pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html' , {'product' : product})


def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

# class ProfileView(View):
#     def get(self, request):
#         form = CustomerProfileForm()
#         return render(request, 'app/profile.html' , {'form' : form, 'active' : 'btn-primary'})

class ProfileView(View):
	def get(self, request):
         form = CustomerProfileForm()
         return render(request, 'app/profile.html' , {'form' : form, 'active' : 'btn-primary'})
		
	def post(self, request):
		form = CustomerProfileForm(request.POST)
		if form.is_valid():
			usr = request.user
			name  = form.cleaned_data['name']
			locality = form.cleaned_data['locality']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			zipcode = form.cleaned_data['zipcode']
			reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
			reg.save()
			messages.success(request, 'Congratulations!! Profile Updated Successfully.')
		return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})







def address(request):
    details= Customer.objects.filter(user= request.user)
    return render(request, 'app/address.html' , {'details' : details , 'active' : 'btn-primary'}) 

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
            return render(request, 'app/customerregistration.html')

        context = {'form' : form}
        return render(request, 'app/customerregistration.html' , context )
        
        


def checkout(request):
 return render(request, 'app/checkout.html')
