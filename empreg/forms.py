
from django import forms

from .models import *

class EmployeeForm(forms.ModelForm):


    class Meta:
        model =Employee
        fields= ('fullname' , 'mobile', 'emp_code' ,'position')
        labels= {
            'fullname' : 'Full Name',
            'mobile' : 'Mobile Number',
            'emp_code' : 'Employee Code',
            'position' : 'Select Position',


        }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select Position" # type: ignore




class LoginForm(forms.ModelForm):
    class Meta:
        model =user_reg
        fields= ('username' , 'password')
        labels= {
            'username' : 'User Name',
            'password' : 'Password',

        }
        



class regForm(forms.ModelForm):
    class Meta:
        model =user_reg
        fields= ('name','username' , 'password')
        labels= {
             'name' : 'Name',
            'username' : 'User Name',
            'password' : 'Password',

        }
 