from django.contrib import admin
from django.urls import path, include
from head import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
    path('customerclick', views.customerclick_view),
    path('customerlogin', LoginView.as_view(template_name='customer/customerlogin.html'),name='customerlogin'),
    path('customersignup', views.customer_signup_view,name='studentsignup'),
    path('customer-dashboard', views.customer_dashboard_view,name='student-dashboard'),
]
