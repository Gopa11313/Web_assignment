from django.shortcuts import render, redirect

from Admin.authenticate import Authenticate
from Admin.forms import AdminForm
from Admin.models import Customer
from Admin.models import Admin
from .models import Employee
from django.http import HttpResponse,JsonResponse


def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/Aboutfiness.html')

def book(request):
    return render(request, 'pages/Book.html')

def contact(request):
    return render(request, 'pages/Contact.html')

def package(request):
    return render(request, 'pages/Package.html')

def service(request):
    return render(request, 'pages/Services.html')

def adminlogin(request):
    return render(request, 'admin/adminlogin.html')

def EmployeeRegistrations(request):
    firstname = request.POST["Frist_name"]
    lastname = request.POST["Last_Name"]
    address = request.POST["address"]
    email = request.POST["email"]
    contact = request.POST["contact"]
    position = request.POST["position"]
    employee_form = Employee(first_name=firstname, last_name=lastname, address=address, email=email, contact=contact,
                             position=position)
    employee_form.save()
    return render(request, 'admin/admin.html')

def CustomerRegistrations(request):
    firstname = request.POST["Frist_name"]
    lastname = request.POST["Last_Name"]
    address = request.POST["address"]
    email = request.POST["email"]
    password = request.POST["password1"]
    service = request.POST["service"]
    customer_form = Customer(first_name=firstname, last_name=lastname, address=address, email=email, password=password,
                             service=service)
    customer_form.save()
    return render(request,'pages/Book.html')

def admin1(request):
    page=1
    limit=3
    if request.method=="POST":
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:
            page=(int(request.POST['page'])-1)
        tempoffset = page - 1
        offset = tempoffset * limit
        employees = Employee.objects.raw("select* from admin_employee limit 3 offset %s", [offset])
        customers = Customer.objects.raw("select * from admin_customer limit 3 offset %s", [offset])
        admins = Admin.objects.raw("select * from admin_admin limit 3 offset %s",[offset])
    else:
        employees = Employee.objects.raw("select* from admin_employee limit 3 offset 0")
        customers = Customer.objects.raw("select * from admin_customer limit 3 offset 0")
        admins = Admin.objects.raw("select * from admin_admin limit 3 offset 0")
    return render(request, 'admin/admin.html', {'employee': employees,'customer': customers,'admin': admins,'page':page})

def entry(request):
    request.session['email'] = request.POST["email"]
    request.session['password'] = request.POST["password"]
    customers = Customer.objects.get(email=request.session['email'])
    id = customers.Customer_id
    return redirect("/customer/'" + str(id) + "'")


def adminentry(request):
    request.session['email'] = request.POST["email"]
    request.session['password'] = request.POST["password"]
    return redirect('/admin1')

def admincreate(request):
    if request.method == "POST":
        form = AdminForm(request.POST, request.FILES)
        form.save()
        return redirect("/adminlogin")
    form = AdminForm()
    return render(request, 'admin/admincreate.html', {'form': form})

def edit(request, id):
    employees = Employee.objects.get(employee_id=id)
    return render(request, 'admin/edit.html', {'employees': employees})

def update(request, id):
    employee = Employee.objects.get(employee_id=id)
    employee_id = id
    firstname = request.POST["Frist_name"]
    lastname = request.POST["Last_Name"]
    address = request.POST["address"]
    email = request.POST["email"]
    contact = request.POST["contact"]
    position = request.POST["position"]
    employee_form = Employee(employee_id=employee_id, first_name=firstname, last_name=lastname, address=address,
                             email=email, contact=contact, position=position)
    employee_form.save()
    return redirect("/admin1")


def delete(request, id):
    Employee.objects.get(employee_id=id)
    user = Employee.objects.get(employee_id=id)
    user.delete()
    return redirect("/admin1")

@Authenticate.valid_user
def customerlogin(request, id):
    customers = Customer.objects.get(Customer_id=id)
    return render(request, 'admin/Customer.html', {'customers': customers})


def employeesearch(request):
    employee=Employee.filter(email=request.GET['employeesearch']).values()
    return JsonResponse(list(employee),safe=False)
def Customersearch(request):
    customer=Customer.filter(email=request.GET['Customersearch']).values()
    return JsonResponse(list(customer),safe=False)
