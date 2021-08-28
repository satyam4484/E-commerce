from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

# these the modesl for main Category of the product 
class Category(models.Model):
    category = models.CharField(max_length=200) # <---------------------|
    image = models.ImageField(upload_to='Category/')  #                 |
    def __str__(self) -> str:     #                                     |
        return self.category #                                          |
#                                                                       |
# these is model for the subcategory of the product                     |
class SubCategory(models.Model):  #                                     |
    Category = models.ForeignKey(Category,on_delete=models.CASCADE) #<--|<----|
    subcat = models.CharField(max_length=200)   #                             |
    subimage = models.ImageField(upload_to='Category/subcategory/') #         |
                                        #                                     |
    def __str__(self) -> str:           #                                     |
        return self.subcat              #                                     |
                                        #                                     |
# These is model for the product details                                      |
class Product(models.Model):                    #                             |
    ProductName= models.CharField(max_length=200)        #                    |
    ProductPrice = models.IntegerField()                 #                    |
    discountprice = models.FloatField(blank=True,null=True) #                 |
    ProductDesc = models.CharField(max_length=2000)         #                 |
    ProductCat = models.ForeignKey(SubCategory,on_delete=models.CASCADE) # <--|
    slug = models.SlugField(null=False,unique=True)
    image = models.FileField(blank=True,upload_to='ProductImage/')

    def __str__(self) -> str:
        return self.ProductName
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
    
# if some user add item to cart then it create a object of that 
class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.BooleanField(default=True)
    isordered = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product}"
    
    def get_total_price(self):
        return self.quantity * self.product.ProductPrice

# model to store all address of different users 
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pincode = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=500,blank=True)

    def __str__(self) -> str:
        return f"{self.address}"

# is somone book the items then these model is used which contains all the neccessary thing about the order 
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.ForeignKey(Address,on_delete=models.SET_NULL,blank=True,null=True)
    item_processed = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user.username}'
    def getdate(self) :
        return self.ordered_date.strftime("%d/%m/%Y")
    def get_final_price(self):
        total = 0
        for items in self.item.all():
            total+=items.get_total_price()
        return total