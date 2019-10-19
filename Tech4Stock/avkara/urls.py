from django.urls import path
from avkara import views

app_name = 'avkara'

urlpatterns = [
    path('signup_seller', views.signup_seller),
    path('signup_vendor', views.signup_vendor),
    path('login/', views.login, name = 'login'),
    path('vendors_list', views.vendors_list, name='VendorsList'),
]
