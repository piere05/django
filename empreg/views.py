from django.shortcuts import redirect, render
from .forms import EmployeeForm
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

