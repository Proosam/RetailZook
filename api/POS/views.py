from django.shortcuts import render
from .serializers import *
from rest_framework import generics,viewsets
from rest_framework.response import Response
from .models import *
from django.db.models  import Sum

class SalesBillAPI(generics.GenericAPIView):
    serializer_class =SalesMainSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "Message":"Bill Generated Successfully",
            "bill": BillingSalesMainSerializer(user, context=self.get_serializer_context()).data
            })
class SlipbillAPI(generics.GenericAPIView):
    serializer_class =EmployeeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "Message":"salry Generated Successfully",
            "bill": SlipbillSerializering(user, context=self.get_serializer_context()).data
            })

class PurchaseBillAPI(generics.GenericAPIView):
    serializer_class = PurchaseMainSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "Message":"Bill Generated Successfully",
            "bill":BillingPurchaseMainSerializer(user, context=self.get_serializer_context()).data })

class CustomersViewSet(viewsets.ModelViewSet):
    serializer_class = PartySerializer
    
    def get_queryset(self):
        queryset = Party.objects.filter(partyType='C')
        return queryset

class SuppliersViewSet(viewsets.ModelViewSet):
    serializer_class = PartySerializer
    
    def get_queryset(self):
        queryset = Party.objects.filter(partyType='S')
        return queryset

class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.filter()
        return queryset

class UOMsViewSet(viewsets.ModelViewSet):
    serializer_class = UOMSerializer
    queryset = UOM.objects.all()
class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
class EmployeepayViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeepaySerializer
class SalaryslipViewSet(viewsets.ModelViewSet):
    serializer_class =  SalaryslipSerializer
class DashboardViewSet(viewsets.ModelViewSet):
    serializer_class =  DashboardSerializer
    
class SalesBillsReportAPI(generics.ListAPIView):
    serializer_class = BillingSalesMainSerializer

    def get_queryset(self):
        import datetime
        from_date = self.request.query_params.get('from_date',None)
        to_date = self.request.query_params.get('to_date',None)
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        queryset = SalesMain.objects.filter(billedDateTime__range=(today_min, today_max))
        if from_date is not None and to_date is not None:
            from_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')
            to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')
            queryset = SalesMain.objects.filter(billedDateTime__range=(from_date, to_date))
        return queryset

class PurchaseBillReportAPI(generics.ListAPIView):
    serializer_class = BillingPurchaseMainSerializer

    def get_queryset(self):
        import datetime
        from_date = self.request.query_params.get('from_date',None)
        to_date = self.request.query_params.get('to_date',None)
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        queryset = PurchaseMain.objects.filter(billedDateTime__range=(today_min, today_max))
        if from_date is not None and to_date is not None:
            from_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')
            to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')
            queryset = PurchaseMain.objects.filter(billedDateTime__range=(from_date, to_date))
        return queryset

class SalesItemWiseReportAPI(generics.ListAPIView):
    serializer_class = ItemWiseSerializer

    def get_queryset(self):
        itemWiseSales = SalesSub.objects.values('product','product__name','product__sellingPrice','product__costPrice','product__uom').annotate(sum_quantity = Sum('quantity')).annotate(sum_taxAmount=Sum('taxAmount')).annotate(sum_netAmount=Sum('netAmount'))
        return itemWiseSales

class PurchaseItemWiseReportAPI(generics.ListAPIView):
    serializer_class = ItemWiseSerializer

    def get_queryset(self):
        itemWiseSales = PurchaseSub.objects.values('product','product__name','product__sellingPrice','product__costPrice','product__uom').annotate(sum_quantity = Sum('quantity')).annotate(sum_taxAmount=Sum('taxAmount')).annotate(sum_netAmount=Sum('netAmount'))
        return itemWiseSales





