from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib import messages


from .models import Employee
# Create your views here.
def emp_lits(request):
    context = {'employee_list' : Employee.objects.all()}
    return render(request,'emp_reg/emp_list.html' , context)


def emp_form(request,id=0):

    if request.method =="GET":
        if id==0:
            form=EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form=EmployeeForm(instance=employee)
        return render(request,'emp_reg/emp_forms.html',{'form' :form})
    else:
        if id==0:
            form=EmployeeForm(request.POST)
        else:
             employee = Employee.objects.get(pk=id)
             form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('view')

def emp_delete(request,id=0):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('view') 



def loginpage(request):
    form=LoginForm()
    return render(request,'index.html', {'form' :form})


def register(request):
    if request.method =="GET":
        form=regForm()
        return render(request,'register.html', {'form' :form})
    else:
        form=regForm(request.POST)
        if form.is_valid():
                obj = form.save(commit=False)
                obj.user_type = 1
                obj.status = 1
                obj.password = make_password(form.cleaned_data["password"])
                obj.save()
                messages.success(request,"User registered successfully")
                return redirect('login')
        else:
            messages.error(request,"Registration failed. Please check your inputs.")
            return redirect('register')

    
