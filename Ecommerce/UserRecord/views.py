from django.http.response import  HttpResponseRedirect
from django.shortcuts import render
from .forms import (UserSignUpForm,UserLoginForm,ChangePasswordForm,userchangeform,profileform)
from django.contrib import messages
from .models import (Userprofile,Wishlist)
from Products.models import Order,Address, Product
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User

# Create your views here.
# /************************* Add to wishlist ************************************\
def AddWishlist(request,id):
    if request.user.is_authenticated:
        wish = Wishlist.objects.create(user=request.user,product = Product.objects.get(pk=id))
        wish.save()
        messages.success(request,'Item Added Successfully')
        return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')
    else :
        messages.error(request,"You should be login to add to wishlist")
        return HttpResponseRedirect('/auth/login')

def RemoveFromWishlist(request,id):
    item = Wishlist.objects.get(product=Product.objects.get(pk=id))
    item.delete()
    messages.success(request,"removed successfully ")
    return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')

# /************************* User Sign up************************************\
def UserSignUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            signup = UserSignUpForm(request.POST)
            if signup.is_valid():
                signup.save()
                return HttpResponseRedirect('/auth/login')
        else :
            signup = UserSignUpForm()
        
        context = {
            'Form':signup,
        }
        return render(request,'Users/signup.html',context)
    else :
        return HttpResponseRedirect('/')

# /************************* User Login up************************************\
def UserLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            Loginform = UserLoginForm(request,data =request.POST)
            if Loginform.is_valid():
                username = Loginform.cleaned_data['username']
                password= Loginform.cleaned_data['password']

                user = authenticate(username = username,password = password)
                
                if user :
                    login(request,user)
                    return HttpResponseRedirect('/')
        else :
            Loginform = UserLoginForm()
        context = {
            "Form":Loginform,
        }
        return render(request,'Users/login.html',context)
    else :
        return HttpResponseRedirect('/')

def ChangePassword(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            changepass = ChangePasswordForm(request.user,request.POST)
            if changepass.is_valid():
                user = changepass.save()
                update_session_auth_hash(request,user)
                messages.success(request,"password Changed Successfully")
                return HttpResponseRedirect('/auth/profile')
        else:
            changepass = ChangePasswordForm(request.user)
        context = {
            'form':changepass
        }  
        return render(request,'Users/changepassword.html',context)
    else:
        return HttpResponseRedirect('/auth/login')

# /************************* User Logout ************************************\

def UserLogout(request):
    logout(request)
    return HttpResponseRedirect('/')

# /************************* Edit User profile ************************************\

def EditUserProfile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form1 = userchangeform(request.POST,instance = request.user)
            form2 = profileform(request.POST,instance=Userprofile.objects.get(pk=request.user))
            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save()
                return HttpResponseRedirect('/auth/profile')
        else :
            form1 = userchangeform(instance = request.user)
            form2 = profileform(instance=Userprofile.objects.get(pk=request.user))
        context = {
            'form1':form1,
            'form2':form2,
        }

        return render(request,'Users/editprofile.html',context)
    else :
        return HttpResponseRedirect('/')

# /************************* User Page ************************************\

def UserprofilePage(request):
    user= User.objects.filter(username=request.user)
    profile = Userprofile.objects.get(pk=request.user)
    userorder =Order.objects.filter(user =request.user)
    wishlist = Wishlist.objects.filter(user=request.user)
    orders = list()
    for order in userorder:
        for data in order.item.all():
            orders.append(data)
            # print(data.product.ProductPrice)
    address = Address.objects.filter(user = request.user)
    context = {
        'profile':profile,
        'orders':userorder,
        'orderdetail':orders,
        'address':address,
        'wishlist':wishlist
    } 
    return render(request,"Users/profile.html",context)

# to be implemeted cart and add isordered fiel in models 