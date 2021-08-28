app_name = ''
from django.urls import path
# include the required views from the user 
from .views import (home,Contact,ShowCart,RemoveFromCart,Searchitem,autocomplete)

urlpatterns = [
    path('',home,name='home'),
    path('contact/',Contact,name='contact'),
    path('Cart/',ShowCart,name='cart'),
    path('removeitem/<int:id>',RemoveFromCart,name='removeitem'),
    path('Search/',Searchitem,name='search'),
    path('autocomplete/',autocomplete,name='autocomplete')
]
