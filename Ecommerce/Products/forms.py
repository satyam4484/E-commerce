from django import forms
from django.db.models import fields
from django.http import request
from .models import Address

COUNTRY = (
    ("India","India"),
)

STATE_CHOICES = (
   ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
   ("Andhra Pradesh","Andhra Pradesh"),
   ("Arunachal Pradesh","Arunachal Pradesh"),
   ("Assam","Assam"),
   ("Bihar","Bihar"),
   ("Chhattisgarh","Chhattisgarh"),
   ("Chandigarh","Chandigarh"),
   ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
   ("Daman and Diu","Daman and Diu"),
   ("Delhi","Delhi"),
   ("Goa","Goa"),
   ("Gujarat","Gujarat"),
   ("Haryana","Haryana"),
   ("Himachal Pradesh","Himachal Pradesh"),
   ("Jammu and Kashmir","Jammu and Kashmir"),
   ("Jharkhand","Jharkhand"),
   ("Karnataka","Karnataka"),
   ("Kerala","Kerala"),
   ("Ladakh","Ladakh"),
   ("Lakshadweep","Lakshadweep"),
   ("Madhya Pradesh","Madhya Pradesh"),
   ("Maharashtra","Maharashtra"),
   ("Manipur","Manipur"),
   ("Meghalaya","Meghalaya"),
   ("Mizoram","Mizoram"),
   ("Nagaland","Nagaland"),
   ("Odisha","Odisha"),
   ("Punjab","Punjab"),
   ("Pondicherry","Pondicherry"),
   ("Rajasthan","Rajasthan"),
   ("Sikkim","Sikkim"),
   ("Tamil Nadu","Tamil Nadu"),
   ("Telangana","Telangana"),
   ("Tripura","Tripura"),
   ("Uttar Pradesh","Uttar Pradesh"),
   ("Uttarakhand","Uttarakhand"),
   ("West Bengal","West Bengal")
)

# form to edit the Address 
class EditAddressForm(forms.ModelForm):
    pincode = forms.CharField(label_suffix=' ',label='Pincode',widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(label_suffix=' ',label='City Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    state = forms.ChoiceField(label_suffix=' ',label='State',choices=STATE_CHOICES)

    country = forms.ChoiceField(label_suffix=' ',label='Country',choices=COUNTRY)
    address=forms.CharField(label='Address',label_suffix=' ',widget=forms.Textarea(attrs={'class':'form-control','rows':3}))

    field_order=['country','state','city','pincode','address']
    class Meta:
        model = Address
        fields=['pincode','city','state','country','address']



       

