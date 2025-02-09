from django.core.validators import RegexValidator
from django.db import models


class PhoneValidator(RegexValidator):
    message = 'Номер телефона должен быть в формате XXX-XXXXXXX или +X XXX-XXXXXXX'
    regex = r'^[+]?[0-9]{1,4}?[-\s\.]?([0-9]{1,5}[-\s\.]?){1,2}$'


class Branch(models.Model):
    branch_address = models.CharField(max_length=255)
    short_name = models.CharField(max_length=125)


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=False, validators=[PhoneValidator])
    # , default = '1970-01-01'
    birthday = models.DateField(auto_now_add=True, blank=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

class Department(models.Model):
    departament_name = models.CharField(max_length=255)
    floor =  models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


