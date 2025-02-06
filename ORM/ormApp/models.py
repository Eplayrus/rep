from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=False)
    birthday = models.DateField(auto_now_add=True, blank=False)

class Departament(models.Model):
    departament_name = models.CharField(max_length=255)
    floor =  models.IntegerField()

class Branch(models.Model):
    branch_address = models.CharField(max_length=255)
    shor_name = models.CharField(max_length=125)

Employee.branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
Departament.branch = models.ForeignKey(Branch, on_delete=models.CASCADE)