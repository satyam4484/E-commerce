from django.urls import path
from .views import (ViewProductDetail,ViewProductList,ViewProductCategory,DeleteAddress,EditAddress,AddItemToCart,CheckoutItem)

urlpatterns = [
    path('catge/<int:id>',ViewProductCategory,name='viewcatgeory'),
    path('subcat/<int:id>',ViewProductList,name='viewproductlist'),
    path('product/<int:id>',ViewProductDetail,name='viewproductdetail'),
    path('DeleteAddress/<int:id>',DeleteAddress,name='deladdress'),
    path('EditAddress/<int:id>',EditAddress,name='editaddress'),    #these will edit the old address 
    path('EditAddress/',EditAddress,name='editaddress'),  # these will add new address 
    path('AddToCart/<int:id>',AddItemToCart,name='cart'),
    path('Checkout/',CheckoutItem,name='checkout'),
]
