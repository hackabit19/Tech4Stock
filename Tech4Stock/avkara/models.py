from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.
class SellerDetails(models.Model):
    name = models.CharField(max_length = 64)
    username = models.OneToOneField(User, on_delete = models.CASCADE)
    mobile_number = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(10)])
    address = models.CharField(max_length = 128)
    def __str__(self):
        return self.username.username

class VendorDetails(models.Model):
    name = models.CharField(max_length = 64)
    username_vendor = models.OneToOneField(User, on_delete = models.CASCADE)
    mobile_number = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(10)])
    #switch = models.BooleanField(default=False)

    def __str__(self):
        return self.username_vendor.username
