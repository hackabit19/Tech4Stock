from django import forms
from avkara.models import SellerDetails, VendorDetails
from django.contrib.auth.models import User

class SellerDetailsForm(forms.ModelForm):

    class Meta:
        model = SellerDetails
        fields = ('name', 'mobile_number', 'address')


class VendorDetailsForm(forms.ModelForm):

    class Meta:
        model = VendorDetails
        fields = ('name', 'mobile_number')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')
