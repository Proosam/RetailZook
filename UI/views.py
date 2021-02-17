from django.shortcuts import render,redirect
from django.contrib.auth import login,get_user_model,logout
from api.POS.models import SalesMain,SalesSub,PurchaseMain,PurchaseSub,UOM,Employee

def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
            if user.check_password(password):
                login(request,user)
                return redirect('/Home')
        except UserModel.DoesNotExist:
            return redirect('/')

    return render(request,'retail/login.html')

def Purchase(request):
    return render(request,'retail/Purchase.html')

def sales(request):
    return render(request,'retail/sales.html')

def Inventory(request):
    uoms = UOM.objects.all()

    
    return render(request,'retail/inventory.html',{
        "uoms":uoms
    })

def Customers(request):
    return render(request,'retail/customers.html')

def Suppliers(request):
    return render(request,'retail/suppliers.html')
def Employee(request):
    return render(request,'retail/employee.html')
def Employeepay(request):
    
  
    return render(request,'retail/employeepay.html')
        
    
def Salaryslip(request):

    Slip_id = request.GET.get('id')
    bill_type = request.GET.get('type')
    context ={}
    if bill_type == "":
        MainObj = Employee.objects.get(id=bill_id)
        SubObj = Employee.objects.filter(mainBill=MainObj)
        context["BillHeader"] = MainObj
        context["BillItems"] = SubObj
        context["type"] = bill_type
    return render(request,'retail/salaryslip.html')
def UOMs(request):
    return render(request,'retail/uoms.html')

def Home(request):
    return render(request,'retail/home.html')
def Dashboard(request):
    return render(request,'retail/dashboard.html')
def Reports(request):
    return render(request,'retail/reports.html')

def invoice(request):
    bill_id = request.GET.get('id')
    bill_type = request.GET.get('type')
    context ={}
    if bill_type == "S":
        MainObj = SalesMain.objects.get(id=bill_id)
        SubObj = SalesSub.objects.filter(mainBill=MainObj)
        context["BillHeader"] = MainObj
        context["BillItems"] = SubObj
        context["type"] = bill_type
    elif bill_type == "P":
        MainObj = PurchaseMain.objects.get(id=bill_id)
        SubObj = PurchaseSub.objects.filter(mainBill=MainObj)
        context["BillHeader"] = MainObj
        context["BillItems"] = SubObj
        context["type"] = bill_type
    
    print(context)
    return render(request,'retail/invoice.html',context)

def signOut(request):
    logout(request)
    return redirect('/')