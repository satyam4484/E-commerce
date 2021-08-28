from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
from Products.models import Product
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


class Userprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    mobileno = models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length=50)

    def getusername(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    def __str__(self) -> str:
        return self.getusername()
    def getuserorder(self):
        return self.myorder

@receiver(post_save, sender=User)
def create_user_profile(sender, instance,created,**kwargs):
    if created:
        Userprofile.objects.create(user=instance)
        name = instance.first_name if instance.first_name else "No name given"
        subject = "A new user has joined our eccomerce"
        message= f'Name : {name} \n Username:{instance.username}'
        # message+='---'*30
        send_mail (subject,message,settings.EMAIL_HOST_USER,[instance.email,],fail_silently=False)

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.OneToOneField(Product,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} wishes {self.product.ProductName}'