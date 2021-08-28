from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import  render
from django.contrib import messages
from Products.models import Address, Product,Category,SubCategory,OrderItem
import datetime 
from django.core.paginator import Paginator

# ************************** Home page  *******************************************************************
def home(request):
    '''
    Url for the home page of the project 
    actions performed --> 
        1: display all products catgeory and attach links to it 
        2: Display all subcategory of products with their images 
        3:list the usercart items if present 
    '''
    cat = Category.objects.all() # fetch all Category of products 

    # fetch subcategrory for each category and store it in key value pairs 
    data = {}
    for ca in cat:
        val = SubCategory.objects.filter(Category__id = ca.id)
        if val:
            data[ca] = val
    # try to fetch user cart if there is item else return empty values 
    try:
        usercart = OrderItem.objects.filter(user=request.user,isordered=False).count()
    except:
        usercart = 0
    
    # all data to be sent to html files 
    context = {
        "category":cat,
        'cartcount':usercart,
        'totalitems':data,
    }
    return render(request,'Home/home.html',context)

# ************************** Contact page  *******************************************************************

def Contact(request):
    '''
        Contact page for user services to be implemented more 
    '''
    return render(request,'Home/contact.html')

# ************************** Show user Cart items   *******************************************************************

def ShowCart(request):
    '''
    It display all the items present in user cart by fetching through user id if he his login 

    '''
    if request.user.is_authenticated:

        # get the current date so that we may delivered the product after 4 days if user buys that product 
        Date1 = datetime.date.today() + datetime.timedelta(days=4)

        # filter user cart which items are not ordered
        try:
            usercart = OrderItem.objects.filter(user=request.user,isordered=False)
        except:
            usercart = []
        
        # these get the total amount of items present in cart 
        totalamount = 0
        for data in usercart:
            totalamount +=data.get_total_price()

        # get all the address provided by user for furthur use 
        address = Address.objects.filter(user = request.user)

        # all data to be passed in the form 
        context = {
            'cartitem':usercart,
            'delivery':f'{Date1.day} { Date1.strftime("%b")} ,{Date1.strftime("%A")}',  # it looks like 'item will deliver by 21 Aug thursday 
            'amount':totalamount,
            'cartcount':len(usercart),
            'address':address,
        }
        return render(request,"Home/showcart.html",context)
    else :
        messages.error(request,"You must login first to add items to cart ")
        return HttpResponseRedirect('/auth/login/')


# ************************** Remove user Cart items   *******************************************************************
def RemoveFromCart(request,id):
    ''' Remove the user items from the cart if user wishes to remove them '''
    product = OrderItem.objects.get(pk=id)
    product.delete()
    # f'{request.META.get("HTTP_REFERER")}'    # these method return previous url from where user is coming so it will redirect him to there 
    return HttpResponseRedirect( f'{request.META.get("HTTP_REFERER")}')


# ************************** Auto complete for search box    *******************************************************************
def autocomplete(request):
    '''
    These function is for the search functionality which provide auto complete feature 
    by fetching data from the models.
    It uses ajax and through jquery is passes asynchronour request and accept the json response 
    '''
    # get the current term which user is typing 
    query = request.GET.get('term')
    # first get all Subcategory from products models 
    catset  =SubCategory.objects.filter(subcat__icontains = query)
    querylist = []
    # append all data in form of string since it will display in form of string 
    querylist+=[x.subcat for x in catset]

    # fetch all Category from the models 
    catset  =Category.objects.filter(category__icontains = query)
    # append all category to query list 
    querylist+=[x.category for x in catset]
    # also search for all products according to query name 
    catset  =Product.objects.filter(ProductName__icontains = query)
    # append it to the list 
    querylist+=[x.ProductName for x in catset]
    # finally return list of string as json to show suggestions at the runtime
    return JsonResponse(querylist,safe=False)
    
# ************************** Search the product    *******************************************************************

def Searchitem(request):
    '''
    Search the data in products models and return 
     -> used little complicated query since don't want user to get record not found so search from all types of models 
        related to product 
    '''
    # get the query from the user 
    query = request.GET.get('query')

    # these will contain all the record according to user query 
    listdata = []
    # if string is not null 
    if query:
        # first search for Category 
        cat = Category.objects.filter(category__icontains = query)
        # if there is some item in Cat then search for its subcategory 
        if cat:
            # traverse all the category items and fin the subcatefory related to this category 
            for itm in cat:
                data = SubCategory.objects.filter(Category__id = itm.id)
                # traverse the subcategory and search for thr products related to this Subcategory 
                for items in data:
                    listdata.extend(Product.objects.filter(ProductCat=items.id))
        # -----------------------------------------------------------------------------------------
        # else search for subcategory 
        else :
            # search for the subcategory items 
            data = SubCategory.objects.filter(subcat__icontains=query)
            # if found similar to that then fint the products related to it 
            if data:
                for items in data:
                    listdata.extend(Product.objects.filter(ProductCat=items.id))
            # else direct search for product in the models and append to list 
            else:
                item = Product.objects.filter(ProductName__icontains = query)
                for items in item:
                    listdata.append(items)

    # /* -------------- Need to Fix these ------------------------\
    # these code is for the paginator which don't work 
    paginator = Paginator(listdata,6)
   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # /* -------------- Need to Fix these ------------------------\
    context = {
        'products':listdata,
        'query':query
        }
    return render(request,'Home/search.html',context)
    

# ************************** End of home views   *******************************************************************
