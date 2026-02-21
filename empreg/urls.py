from django.urls import path

from . import views


urlpatterns = [
    path('', views.emp_form,name="insert"),
    path('<int:id>/', views.emp_form,name="update"),
    path('list/', views.emp_lits,name="view"),
    path('delete/<int:id>/', views.emp_delete,name="delete"),

]
