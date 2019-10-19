from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from avkara.forms import UserForm, SellerDetailsForm, VendorDetailsForm
from django.urls import reverse
from .models import VendorDetails
from django_twilio.decorators import twilio_view
from twilio.twiml.messaging_response import MessagingResponse

# Create your views here.
def index(request):
    return render(request, 'avkara/index.html')

def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if request.method=='POST':
        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect(reverse('avkara:VendorsList'))

            else:

                return HttpResponse('Something is wrong!')
        else:

            return HttpResponse('Incorrect details')
    else:

        return render(request, 'avkara/login.html')

def logout_user(request):
    logout(request)
    return render(request, 'avkara/logout_page.html')

def signup_seller(request):
    seller_registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        seller_form = SellerDetailsForm(data= request.POST)
        if user_form.is_valid() and seller_form.is_valid():
            seller= user_form.save()

            seller.set_password(seller.password)

            seller.save()
            #now saving other informatiohn
            seller_other_info = seller_form.save(commit = False)
            seller_other_info.username = seller
            seller_other_info.save()
            seller_registered = True
    else:
        user_form = UserForm()
        seller_form = SellerDetailsForm()
    return render(request, 'avkara/signup_seller.html', {'user_form': user_form, 'seller_form': seller_form, 'seller_registered': seller_registered})

def signup_vendor(request):
    vendor_registered = False
    if request.method == 'POST':
        user_form_vendor = UserForm(data=request.POST)
        vendor_form = VendorDetailsForm(data= request.POST)
        if user_form_vendor.is_valid() and vendor_form.is_valid():
            vendor= user_form_vendor.save()

            vendor.set_password(vendor.password)

            vendor.save()
            #now saving other informatiohn
            vendor_other_info = vendor_form.save(commit = False)
            vendor_other_info.username_vendor = vendor
            vendor_other_info.save()
            vendor_registered = True
    else:
        user_form_vendor = UserForm()
        vendor_form = VendorDetailsForm()
    return render(request, 'avkara/signup_vendor.html', {'user_form_vendor': user_form_vendor, 'vendor_form': vendor_form, 'vendor_registered': vendor_registered})

@login_required
def vendors_list(request):
    allvendors= VendorDetails.objects.all()
    context= {'allvendors': allvendors}
    return render(request, 'avkara/vendors_list.html', context)

@twilio_view
def sms(request):
    r = Response()
    r.message('Hello from your Django app!')
    return r
