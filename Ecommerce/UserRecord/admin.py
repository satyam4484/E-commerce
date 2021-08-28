from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Userprofile)
class UserAdminProfile(admin.ModelAdmin):
    list_display = ['user','mobileno','gender']

# @admin.register(UserAddress)
# class UserAdminAddress(admin.ModelAdmin):
#     list_display = ['Address','country','state','city','pincode']
@admin.register(Wishlist)
class wishadmin(admin.ModelAdmin):
    list_display = ['user','product']