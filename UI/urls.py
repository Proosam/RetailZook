from django.urls import path
from . import views

urlpatterns = [
    path('',views.signIn,name="SignIn"),
    path('Home',views.Home,name="Home"),
    path('Sales',views.sales,name="Sales"),
    path('Purchase',views.Purchase,name="Purchase"),
    path('Inventory',views.Inventory,name="Inventory"),
    path('Customers',views.Customers,name="Customers"),
    path('Suppliers',views.Suppliers,name="Suppliers"),
    path('UOMs',views.UOMs,name="UOMs"),
    path('employee',views.Employee,name="Employee"),
    path('employeepay',views.Employeepay,name="employeepay"),
    path('salaryslip',views.Salaryslip,name="salaryslip"),
    path('Dashboard',views.Dashboard,name="dashboard"),
    path('invoice',views.invoice,name="invoice"),
    path('Reports',views.Reports,name="Reports"),
    path('signOut',views.signOut,name="UOMs"),
]