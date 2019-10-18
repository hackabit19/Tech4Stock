from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request, 'avkara/index.html')

def login(request):
    pass

def signup_seller(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        seller_form = SellerDetailsForm(data= request.POST)
        return HttpResponse('Thank')
    else:
        user_form = UserForm()
        seller_form = SellerDetailsForm()
    return render(request, 'avkara/signup_seller.html', {'user_form': user_form, 'seller_form': seller_form})
