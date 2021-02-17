from django.db import models



class UOM(models.Model):
    unit = models.CharField(max_length=15,default='Unnammed')

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Party(models.Model):
    partyTypes = (('C','Customer'),('S','Supplier'))
    name = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=15,unique=True)
    email = models.EmailField(max_length=50,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    partyType = models.CharField(max_length=1,choices=partyTypes,default='C')

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
class Employee(models.Model):
    name = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=15,unique=True)
    email = models.EmailField(max_length=50,null=True,blank=True)
    salary=models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    photo=models.ImageField(null=True,blank=True)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    sellingPrice = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    costPrice = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    available_stock = models.DecimalField(max_digits=10, decimal_places=2)
    uom = models.CharField(max_length=10)
    tax_percent = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class SalesMain(models.Model):
    customer = models.ForeignKey(Party,on_delete=models.CASCADE,related_name='customers')
    itemCount = models.PositiveIntegerField()
    billedBy = models.CharField(max_length=25)
    billTotal = models.DecimalField(max_digits=10,decimal_places=2)
    totalTax = models.DecimalField(max_digits=10,decimal_places=2)
    discount = models.DecimalField(max_digits=10,decimal_places=2)
    netTotal = models.DecimalField(max_digits=10,decimal_places=2)
    paymentType = models.CharField(max_length=25)
    status = models.CharField(max_length=25)
    billedDateTime = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateField(auto_now=True)

class SalesSub(models.Model):
    mainBill=models.ForeignKey(SalesMain,on_delete=models.CASCADE,related_name="Salesbills")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="Salesproducts")
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10,decimal_places=2)
    taxAmount = models.DecimalField(max_digits=10,decimal_places=2)
    netAmount = models.DecimalField(max_digits=10,decimal_places=2)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class PurchaseMain(models.Model):
    supplier = models.ForeignKey(Party,on_delete=models.CASCADE,related_name='Suppliers')
    itemCount = models.PositiveIntegerField()
    billedBy = models.CharField(max_length=25)
    billTotal = models.DecimalField(max_digits=10,decimal_places=2)
    totalTax = models.DecimalField(max_digits=10,decimal_places=2)
    discount = models.DecimalField(max_digits=10,decimal_places=2)
    netTotal = models.DecimalField(max_digits=10,decimal_places=2)
    paymentType = models.CharField(max_length=25)
    status = models.CharField(max_length=25)
    billedDateTime = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateField(auto_now=True)

class PurchaseSub(models.Model):
    mainBill=models.ForeignKey(PurchaseMain,on_delete=models.CASCADE,related_name="PurchaseBills")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="PurchaseProducts")
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10,decimal_places=2)
    taxAmount = models.DecimalField(max_digits=10,decimal_places=2)
    netAmount = models.DecimalField(max_digits=10,decimal_places=2)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)