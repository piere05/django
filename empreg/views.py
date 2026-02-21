from django.shortcuts import redirect, render
from .forms import *
from .models import Employee, user_reg
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages


from .models import Employee
# Create your views here.
def emp_lits(request):
    if "user_id" not in request.session:
        return redirect('login')
    else:
        context = {'employee_list' : Employee.objects.all()}
        return render(request,'emp_reg/emp_list.html' , context)


def emp_form(request,id=0):
    if "user_id" not in request.session:
        return redirect('login')
    else:
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
    if "user_id" in request.session:
        return redirect('insert')
    else:
        if request.method == "GET":
            form = LoginForm()
            return render(request,'index.html', {'form': form})
        else:
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]

                try:
                    user = user_reg.objects.get(username=username, status=1)

                    if check_password(password, user.password):
                        request.session["user_id"] = user.pk
                        request.session["username"] = user.username
                        request.session["user_type"] = user.user_type
                        return redirect('/emp/')
                    else:
                        messages.error(request,"Invalid password")
                        return redirect('login')

                except user_reg.DoesNotExist:
                    messages.error(request,"User not found")
                    return redirect('login')
            else:
                messages.error(request,"Invalid form data")
                return redirect('login')



def register(request):
    if "user_id"  in request.session:
        return redirect('insert')
    else:
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

    
def logout(request):
    request.session.flush()
    return redirect('login')
