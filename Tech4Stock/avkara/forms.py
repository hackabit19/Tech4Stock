from django import forms
from avkara.models import SellerDetails, VendorDetails

class SellerDetailsForm(forms.ModelForm):

    class Meta:
        model = SellerDetails
        fields = ('name', 'username', 'mobile_number', 'address')


class VendorDetailsForm(forms.ModelForm):

    class Meta:
        model = VendorDetails
        fields = ('name', 'username', 'mobile_number')

class UserForm(object):
    password = forms.CharField(widget = PasswordInput())

    class ClassName(object):
        model = User
        fields = ('username', 'password')
