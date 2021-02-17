from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('customers',views.CustomersViewSet,'customers')
router.register('suppliers',views.SuppliersViewSet,'suppliers')
router.register('products',views.ProductsViewSet,'products')
router.register('uoms',views.UOMsViewSet,'uoms')
router.register('employee',views.EmployeeViewSet,'employee')
router.register('employeepay',views.EmployeepayViewSet,'employeepay')
router.register('salaryslip',views.SalaryslipViewSet,'salaryslip')
router.register('dashboard',views.DashboardViewSet,'Dashboard')
urlpatterns = [
    path('',include(router.urls)),
    path('SalesBill',views.SalesBillAPI.as_view(),name="SalesBillAPI"),
    path('Slipbill',views.SlipbillAPI.as_view(),name="SlipbillAPI"),
    path('PurchaseBill',views.PurchaseBillAPI.as_view(),name="PurchaseBill"),
    path('SalesBillReport',views.SalesBillsReportAPI.as_view(),name="SalesBillsReport"),
    path('PurchaseBillReport',views.PurchaseBillReportAPI.as_view(),name="PurchaseBillsReport"),
    path('SalesItemWise',views.SalesItemWiseReportAPI.as_view(),name="SalesItemWise"),
    path('PurchaseItemWise',views.PurchaseItemWiseReportAPI.as_view(),name="PurchaseItemWise"),
]