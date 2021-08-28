from django.urls import path 
from .views import *

urlpatterns = [
    path('signup/',UserSignUp,name='signup'),
    path('login/',UserLogin,name='login'),
    path('logout/',UserLogout,name='logout'),
    path('profile/',UserprofilePage,name='profile'),
    path('editprofile/',EditUserProfile,name='editprofile'),
    path('changepassword/',ChangePassword,name='changepassword'),
    path('AddWishlist/<int:id>',AddWishlist,name='wishlist'),
    path('RemoveWish/<int:id>',RemoveFromWishlist,name='removewish'),
]
