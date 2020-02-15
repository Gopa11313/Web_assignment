from django.urls import path

from . import views

urlpatterns = [
    path("", views.index,name="Home"),
    path("index", views.index),
    path("Aboutfiness", views.about),
    path("Book", views.book),
    path("Contact", views.contact),
    path("Package", views.package),
    path("Services", views.service),
    path("admin1", views.admin1),
    path("EmployeeRegistrations/", views.EmployeeRegistrations),
    path("CustomerRegistrations/", views.CustomerRegistrations),
    path("edit/<int:id>", views.edit),
    path("update/<int:id>", views.update),
    path("delete/<int:id>", views.delete),
    path("customer/'<int:id>'", views.customerlogin),
    path('entry', views.entry),
    path('adminlogin/', views.adminlogin),
    path('adminentry', views.adminentry),
    path('admincreate', views.admincreate),
    path('adminlogin', views.adminlogin),
    path('employeesearch',views.employeesearch),
    path('Customersearch',views.Customersearch),
    
]
