from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display=['id','category']

@admin.register(SubCategory)
class SubCatAdmin(admin.ModelAdmin):
    list_display=['Category','subcat']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','ProductName','ProductPrice','ProductDesc','ProductCat','slug']
    search_fields=['ProductName',]
    class Meta:
        model = Product
    prepopulated_fields = {'slug': ('ProductName',)}

@admin.register(Address)
class AdressAdmin(admin.ModelAdmin):
    list_display=['user','pincode','city','state','country','address']

@admin.register(OrderItem)
class orderitemAdmin(admin.ModelAdmin):
    list_display=['user','product','quantity']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['user','ordered_date','shipping_address','item_processed','delivered']

# @admin.register(Cart)
# class AdminCart(admin.ModelAdmin):
#     pass