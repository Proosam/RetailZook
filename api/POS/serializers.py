from rest_framework import serializers
from .models import *
from decimal import *

class UOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOM
        fields = '__all__'
class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOM
        fields = '__all__'
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
class EmployeepaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
class SalaryslipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'

class BillingSalesMainSerializer(serializers.ModelSerializer):
    customer = PartySerializer()
    class Meta:
        model = SalesMain
        fields = '__all__'

class BillingSalesSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesSub
        fields = '__all__'
class SlipbillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class BillingPurchaseMainSerializer(serializers.ModelSerializer):
    supplier = PartySerializer()
    class Meta:
        model = PurchaseMain
        fields = '__all__'

class BillingPurchaseSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseSub
        fields = '__all__'

class ItemWiseSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    product__name = serializers.CharField()
    product__uom = serializers.CharField()
    product__sellingPrice = serializers.DecimalField(max_digits=10,decimal_places=2)
    product__costPrice = serializers.DecimalField(max_digits=10,decimal_places=2)
    sum_quantity =serializers.IntegerField()
    sum_taxAmount =serializers.DecimalField(max_digits=10,decimal_places=2)
    sum_netAmount = serializers.DecimalField(max_digits=10,decimal_places=2)

class SalesSubSeializer(serializers.Serializer):
    productId = serializers.IntegerField()
    quantity = serializers.IntegerField()
    total = serializers.DecimalField(max_digits=10,decimal_places=2)
    taxAmount = serializers.DecimalField(max_digits=10,decimal_places=2)
    netAmount = serializers.DecimalField(max_digits=10,decimal_places=2)

class SalesMainSerializer(serializers.Serializer):
    customerId = serializers.IntegerField()
    discount = serializers.DecimalField(max_digits=10,decimal_places=2,required=False)
    products = SalesSubSeializer(many=True)

    def create(self,validated_data):
        data = validated_data
        total = Decimal(0.0)
        total_tax = Decimal(0.0)
        net_amount = Decimal(0.0)
        for product in data["products"]:
            total += product["total"]
            total_tax += product["taxAmount"]
            net_amount += product["netAmount"]
        net_amount = total - data["discount"] + total_tax
        customer = Party.objects.get(id=data["customerId"])
        billMain = SalesMain.objects.create(customer=customer,
        itemCount=len(data["products"]),
        billedBy="Admin",
        totalTax=total_tax,
        discount=data["discount"],
        netTotal=net_amount,
        paymentType="Cash",
        status="Paid",billTotal=total)
        for product in data["products"]:
            pro = Product.objects.get(id=product["productId"])
            billSub = SalesSub(mainBill=billMain,
            product=pro,
            quantity=product["quantity"],
            total=product["total"],
            taxAmount=product["taxAmount"],
            netAmount=product["netAmount"])
            billSub.save()
        return billMain    

class PurchaseSubSeializer(serializers.Serializer):
    productId = serializers.IntegerField()
    quantity = serializers.IntegerField()
    total = serializers.DecimalField(max_digits=10,decimal_places=2)
    taxAmount = serializers.DecimalField(max_digits=10,decimal_places=2)
    netAmount = serializers.DecimalField(max_digits=10,decimal_places=2)

class PurchaseMainSerializer(serializers.Serializer):
    supplierId = serializers.IntegerField()
    discount = serializers.DecimalField(max_digits=10,decimal_places=2,required=False)
    products = SalesSubSeializer(many=True)

    def create(self,validated_data):
        data = validated_data
        total = Decimal(0.0)
        total_tax = Decimal(0.0)
        net_amount = Decimal(0.0)
        for product in data["products"]:
            total += product["total"]
            total_tax += product["taxAmount"]
            net_amount += product["netAmount"]
        net_amount = total - data["discount"] + total_tax
        supplier = Party.objects.get(id=data["supplierId"])
        billMain = PurchaseMain.objects.create(supplier=supplier,
        itemCount=len(data["products"]),
        billedBy="Admin",
        totalTax=total_tax,
        discount=data["discount"],
        netTotal=net_amount,
        paymentType="Cash",
        status="Paid",billTotal=total)
        for product in data["products"]:
            pro = Product.objects.get(id=product["productId"])
            billSub = PurchaseSub(mainBill=billMain,
            product=pro,
            quantity=product["quantity"],
            total=product["total"],
            taxAmount=product["taxAmount"],
            netAmount=product["netAmount"])
            billSub.save()
        return billMain    

