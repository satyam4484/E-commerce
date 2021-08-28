# from django.core import paginator
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Products.models import Address, Order, OrderItem, SubCategory,Category,Product
from .forms import EditAddressForm
from django import forms
from django.core.paginator import Paginator
import random

# Create your views here.
# /***************************** View subCategory *******************************************\
def ViewProductCategory(request,id):
    ''' These will display the Category of the followin product which it belongs '''

    # these code is just to get user cart items 
    try:
        usercart = OrderItem.objects.filter(user=request.user,isordered=False).count()
    except:
        usercart = 0
    # fetch all Category of the data request 
    cat = Category.objects.get(pk=id)
    # find all subcategory related that Category of the product 
    ProdSubCat = SubCategory.objects.filter(Category = cat)
    # data to be passed 
    context = {
        "subcategory":ProdSubCat,
        'cartcount':usercart
    }
    return render(request,'products/ViewProductCategory.html',context)

# /***************************** View product related to Subcat   *******************************************\

def ViewProductList(request,id):
    ''' Display the list of item according to the subcategory provided '''
    # same as above function 
    try:
        usercart = OrderItem.objects.filter(user=request.user,isordered=False).count()
    except:
        usercart = 0
    # find the subcategory 
    subcat = SubCategory.objects.get(pk=id)
    # search all products related to that sub cat 
    products = Product.objects.filter(ProductCat=subcat)
    print(subcat.Category)
    # similar product of the Category 
    similarproduct = Product.objects.filter(ProductCat__Category__id=subcat.Category.id ).exclude(ProductCat=subcat)

    context = {
        "products":products,
        'cartcount':usercart,
        'similarprod':similarproduct,
    }
    return render(request,'products/ViewProductList.html',context)

# /***************************** View particular product   *******************************************\

def ViewProductDetail(request,id):

    ''''View particular product in detail with the id of the product '''

    # fetch user cart items 
    try:
        usercart = OrderItem.objects.filter(user=request.user,isordered=False).count()
    except:
        usercart = 0

    # get the product 
    product = Product.objects.get(pk=id)
    # get its category
    cat = product.ProductCat

    # get similar items related to field 
    similar_items = Product.objects.filter(ProductCat__id = cat.id).exclude(pk=id)

    context = {
        "product":product,
        "similarProd":similar_items
    }
    return render(request,'products/viewproductdetail.html',context)

# /***************************** Delete the address of a particular user   *******************************************\

def DeleteAddress(request,id):
    # get the address data and delete it 
    address = Address.objects.get(pk=id)
    address.delete()
    return HttpResponseRedirect('/auth/profile')


# /***************************** Edit the address of a particular user   *******************************************\

def EditAddress(request,id=None):
    ''' These function are combine to edit the address as well to add new address by 
        some logic 
        '''
    if request.method == "POST":
        # get the id if exist ( if then edit the addresss if no then Add new address )
        if id:
            data = Address.objects.get(pk=id)
            form = EditAddressForm(request.POST,instance=data)
        else :
            form = EditAddressForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request,"Successfully added Address")
            return HttpResponseRedirect('/auth/profile')
    else :
        if id:
            data = Address.objects.get(pk=id)
            form = EditAddressForm(instance=data)
        else :
            form = EditAddressForm()
    # fetch user cart items 
    try:
        usercart = OrderItem.objects.filter(user=request.user,isordered=False).count()
    except:
        usercart = 0
    context = {
        'form':form,
        'cartcount':usercart
    }
    
    return render(request,'Users/editaddress.html',context)

# /***************************** Add Items to cart    *******************************************\

def AddItemToCart(request,id):
    ''' These will add item to cart for a particular user '''
    if request.user.is_authenticated:
        product = Product.objects.get(pk=id)
        try:
            order = OrderItem.objects.get(product=product)   
            order.quantity +=1
            order.save()     
        except :
            order = OrderItem.objects.create(user=request.user,product=product)
        messages.success(request,'Item Added Successfully')
        return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')
    else:
        messages.warning(request,'You need to login to add items ')
        return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')


# to be implemented 
def CheckoutItem(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            addr = Address.objects.filter(user=request.user)
            
            address = EditAddressForm(request.POST,instance=addr[0])
            if address.is_valid():
                print("save")
        else :
            addr = Address.objects.filter(user=request.user)
            address = EditAddressForm(instance=addr[0])
        try:
            usercart = OrderItem.objects.filter(user=request.user,isordered=False)
        except:
            usercart = []
        createorder = Order.objects.create(user=request.user)
        createorder.item.set(usercart)
        context = {
            'address':address
        }
        return render(request,'products/checkout.html',context)
    else:
        messages.error(request,"login to buy products")
        return HttpResponseRedirect('/auth/login')