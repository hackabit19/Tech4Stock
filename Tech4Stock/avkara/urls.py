from django.urls import path
from avkara import views

app_name = 'avkara'

urlpatterns = [
    path('signup_seller', views.signup_seller, name = 'signup_seller'),
    path('signup_vendor', views.signup_vendor, name = 'signup_vendor'),
    path('login/', views.login_user, name = 'login'),
    path('vendors_list', views.vendors_list, name='VendorsList'),
    path('logout', views.logout_user, name = 'logout'),
]
