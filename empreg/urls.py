from django.urls import path

from . import views


urlpatterns = [
    path('', views.loginpage,name="login"),
    path('register/', views.loginpage,name="register"),
    path('emp/', views.emp_form,name="insert"),
    path('emp/<int:id>/', views.emp_form,name="update"),
    path('emp/list/', views.emp_lits,name="view"),
    path('emp/delete/<int:id>/', views.emp_delete,name="delete"),

]
