from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(auto_created=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    position = models.CharField(max_length=50)

    class meta:
        db_table = "employee"

class Customer(models.Model):
    Customer_id = models.AutoField(auto_created=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    service = models.CharField(max_length=50)

    class meta:
        db_table = "customer"

class Admin(models.Model):
    admin_id = models.AutoField(auto_created=True, primary_key=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, unique=True)

    class meta:
        db_table = "admin"
